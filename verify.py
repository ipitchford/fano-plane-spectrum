#!/usr/bin/env python3
"""Fail-closed producer replay. Saved artifacts and fresh computations are distinct."""
import argparse
import itertools
import json
import math
from pathlib import Path
import re
import subprocess
import sys
import time
import sympy as s

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'code'))
import macaulay

def require(value, message):
    if not value:
        raise RuntimeError(message)

def read(root, name):
    return json.loads((root / name).read_text())

def artifact_checks(root):
    x = s.Symbol('x')
    factors = [(x,35),(x-1,35),(x-2,28),(x-3,1),(x*x-x+1,7),
        (x*x+2*x+6,7),(x*x+x+1,21),(x*x+x+2,52),
        (x**3+2*x*x+2*x-2,21),(x**4-x**3-x*x+x+1,28)]
    require(all(s.Poly(f,x).is_irreducible for f,_ in factors),'irreducibility')
    poly = s.Poly(s.prod(f**m for f,m in factors),x)
    coeffs = list(map(int,reversed(poly.all_coeffs())))
    require(poly.degree()==448,'degree')
    for name in ['out/phi_H7.json','out30/phi_H7.json']:
        require(read(root,name)['coeffs_low_to_high']==coeffs, 'coefficient mismatch: '+name)
    primes=read(root,'out30/phi_H7.json')['primes']
    require(len(primes)==len(set(primes))==30 and all(s.isprime(p) for p in primes),'prime list')
    M=math.prod(primes)
    require(M>2*4**448,'Fano lift bound')
    residues={int(p):v for p,v in read(root,'out30/h7_per_prime.json').items()}
    require(set(primes)==set(residues),'residue coverage')
    for p,v in residues.items():
        require(v==[c%p for c in coeffs],f'residue mismatch: {p}')
    weights={p:(M//p)*pow(M//p,-1,p) for p in primes}
    for k,c in enumerate(coeffs):
        v=sum(residues[p][k]*weights[p] for p in primes)%M
        require((v-M if 2*v>M else v)==c,f'CRT coefficient {k}')
    edges={tuple(sorted(e)) for e in [(1,2,4),(2,3,5),(3,4,6),(4,5,7),(1,5,6),(2,6,7),(1,3,7)]}
    require(all(sum(set(pair)<=set(e) for e in edges)==1 for pair in itertools.combinations(range(1,8),2)),'Fano pairs')
    induced=[]
    for m in range(1,7):
        d=read(root,f'out/phi_H{m}.json')
        ee={tuple(sorted(e)) for e in d['edges']}
        require(ee=={e for e in edges if max(e)<=m},f'edge encoding H{m}')
        pp=d['primes']; degree=m*2**(m-1)
        require(len(pp)==len(set(pp)) and all(s.isprime(p) for p in pp),f'primes H{m}')
        delta=max(sum(i in e for e in ee) for i in range(1,m+1))
        require(math.prod(pp)>2*(1+delta)**degree,f'inductive lift H{m}')
        require(d['degree']==degree and len(d['coeffs_low_to_high'])==degree+1 and d['coeffs_low_to_high'][-1]==1,f'degree H{m}')
        require(d['coeffs_low_to_high']==read(root,f'out30/phi_H{m}.json')['coeffs_low_to_high'],f'lower-stage copies H{m}')
        induced.append({'m':m,'bound_bits':(2*(1+delta)**degree).bit_length(),'modulus_bits':math.prod(pp).bit_length()})
    saved=read(root,'out/macaulay_full_p2147483647.json')
    require(saved['poly_mod_p']==[c%saved['p'] for c in coeffs],'saved Macaulay polynomial')
    return {'saved_artifacts':'PASS','crt_bits':M.bit_length(),'inductive_bounds':induced,'c14':coeffs[434]}

def run(command):
    p=subprocess.run(command,cwd=ROOT,capture_output=True,text=True,timeout=600)
    require(p.returncode==0,'process failure: '+str(command)+'\n'+p.stdout[-2000:]+p.stderr[-2000:])
    return p.stdout

def singular(name):
    out=run(['Singular','-q',str(ROOT/'verification'/name)])
    require(not re.search(r'^\s*\?',out,re.M),'Singular diagnostic in '+name)
    return out

def fresh_checks():
    vertices=range(1,8)
    edges={frozenset(e) for e in [(1,2,4),(2,3,5),(3,4,6),(4,5,7),(1,5,6),(2,6,7),(1,3,7)]}
    automorphisms=[p for p in itertools.permutations(vertices) if {frozenset(p[i-1] for i in e) for e in edges}==edges]
    require(len(automorphisms)==168 and {p[0] for p in automorphisms}==set(vertices),'automorphisms/transitivity')
    w=s.Symbol('w'); zero_vectors=set(); one_vectors=set()
    def residual(v,lam):
        for i in vertices:
            expr=sum(s.prod(v[j-1] for j in e if j!=i) for e in edges if i in e)-lam*v[i-1]**2
            require(s.rem(s.expand(expr),w*w+w+1,w)==0,'new explicit family')
    # Normalize quadrangle signs by their first nonzero coordinate.
    for edge in edges:
        Q=sorted(set(vertices)-edge)
        for signs in itertools.product([-1,1],repeat=4):
            if math.prod(signs)!=-1: continue
            v=[0]*7
            for i,a in zip(Q,signs): v[i-1]=a
            residual(v,0)
            first=next(a for a in v if a)
            zero_vectors.add(tuple(a*first for a in v))
        for twist in [(1,1,1),(1,w,w*w),(1,w*w,w)]:
            v=[0]*7
            for i,a in zip(sorted(edge),twist): v[i-1]=a
            residual(v,1); one_vectors.add(tuple(v))
    require(len(zero_vectors)==28 and len(one_vectors)==21,'new family class counts')
    out=run([sys.executable,*(['-O'] if sys.flags.optimize else []),str(ROOT/'code/verify_eigenvectors.py')])
    require('ALL OK' in out and 'FAIL' not in out,'symbolic vectors')
    g=singular('geometry_audit.sing')
    require('SATURATED DIM DEGREE\n2\n8\n' in g,'saturated dimension and degree')
    require('(3t2+4t+1) / (1-t)^2' in g,'saturated Hilbert series')
    require('Sat[1]=x1+x2+x3+x4+x5+x6+x7' in g,'hyperplane')
    require('SINGULAR CONE DIM\n0\n' in g,'smoothness')
    require('1,1,0,0,0,0,\n0,7,15,11,3,0,\n0,0,6,14,11,3' in g,'resolution Betti certificate')
    r=singular('reality_audit.sing')
    require(re.search(r'CERTIFICATE RESIDUAL\s+_\[1,1\]=0',r) is not None,'sum of squares identity')
    lengths=singular('chart_lengths.sing')
    require(re.findall(r'LENGTH (\d+) (\d+)',lengths)==[('0','17'),('1','15'),('2','24'),('3','1')],'chart lengths')
    primary=singular('primary_lengths.sing')
    require('COMPONENTS 2 6' in primary and re.findall(r'PRIMARY_RADICAL_LENGTH 2 (\d+) (\d+)',primary)==[('4','2')]*6,'primary versus radical lengths at two')
    require('COMPONENTS 1 6' in primary and sorted(re.findall(r'PRIMARY_RADICAL_LENGTH 1 (\d+) (\d+)',primary))==[('1','1')]*3+[('4','2')]*3,'primary versus radical lengths at one')
    evaluations=[]
    for m,lam,p in [(4,17,1000000007),(5,19,1000000007),(7,457,1000000007),(7,911,2147483629)]:
        value,_,den=macaulay.macaulay_value(m,lam,macaulay.edges_induced(m),p)
        expected=0
        for c in reversed(read(ROOT,f'out/phi_H{m}.json')['coeffs_low_to_high']):
            expected=(expected*lam+c)%p
        require(den and value==expected,f'fresh Macaulay H{m}')
        evaluations.append({'m':m,'lambda':lam,'prime':p,'value':value,'denominator':den})
    return {'symbolic_vectors':'PASS','automorphisms':168,'quadrangle_sign_classes':28,'line_classes_at_one':21,'characteristic_zero_geometry':'PASS','real_obstruction':'PASS','rational_chart_lengths':[17,15,24,1],'primary_radical_lengths_at_two':[[4,2]]*6,'fresh_macaulay':evaluations}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--artifacts-only',action='store_true'); p.add_argument('--root',type=Path,default=ROOT)
    args=p.parse_args(); start=time.monotonic()
    result=artifact_checks(args.root)
    if not args.artifacts_only:
        require(args.root.resolve()==ROOT,'fresh mode uses the installed source root')
        result.update(fresh_checks())
    result.update(status='PASS',wall_seconds=round(time.monotonic()-start,3),optimized=bool(sys.flags.optimize),assurance='Producer-side replay; not a fresh full thirty-prime resultant computation or formal proof.')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
