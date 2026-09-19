"""Semantic corruptions must fail in both ordinary and optimized Python."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
ROOT=Path(__file__).resolve().parent
for optimized in [False,True]:
    prefix=[sys.executable]+(['-O'] if optimized else [])
    for name,file,mutate,expected in [
        ('coefficient','out30/phi_H7.json',lambda d:d['coeffs_low_to_high'].__setitem__(434,d['coeffs_low_to_high'][434]+1),'coefficient mismatch'),
        ('duplicate-prime','out30/phi_H7.json',lambda d:d['primes'].__setitem__(1,d['primes'][0]),'prime list'),
        ('residue','out30/h7_per_prime.json',lambda d:next(iter(d.values())).__setitem__(0,1),'residue mismatch'),
        ('edge','out/phi_H6.json',lambda d:d['edges'].__setitem__(0,[1,2,3]),'edge encoding'),
    ]:
        with tempfile.TemporaryDirectory(prefix='fano-negative-') as tmp:
            root=Path(tmp)
            for directory in ['out','out30']:
                shutil.copytree(ROOT/directory,root/directory)
            target=root/file; data=json.loads(target.read_text()); mutate(data)
            target.write_text(json.dumps(data))
            p=subprocess.run(prefix+[str(ROOT/'verify.py'),'--artifacts-only','--root',str(root)],capture_output=True,text=True,timeout=120)
            if p.returncode==0 or expected not in p.stderr:
                raise RuntimeError('Negative control failed: '+name+'\n'+p.stdout+p.stderr)
        print(f'REJECTED {name} optimized={optimized}')
    with tempfile.TemporaryDirectory(prefix='fano-vector-negative-') as tmp:
        target=Path(tmp)/'vectors.py'
        source=(ROOT/'code/verify_eigenvectors.py').read_text().replace('return sum(x[j]*x[k]', 'return -sum(x[j]*x[k]')
        target.write_text(source)
        p=subprocess.run(prefix+[str(target)],capture_output=True,text=True,timeout=60)
        if p.returncode==0 or 'SOME FAILED' not in p.stdout:
            raise RuntimeError('Wrong-sign eigen-equations were not rejected')
        print(f'REJECTED equation-sign optimized={optimized}')
print('PASS: 10 semantic negative controls')
