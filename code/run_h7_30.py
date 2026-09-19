#!/usr/bin/env python3
"""Recompute phi_{H_7} (the Fano plane) modulo 30 primes, reusing phi_{H_6} from an earlier run,
and lift by CRT.  Deterministic: 30 primes give a modulus > 2^929 > 2 * 4^448, which exceeds twice the
a-priori coefficient bound (all eigenvalues have modulus <= 3)."""
import json, sys, os, time, math
from multiprocessing import Pool
import poisson

outdir = sys.argv[1] if len(sys.argv) > 1 else "out30"
nprimes = int(sys.argv[2]) if len(sys.argv) > 2 else 30
nproc = int(sys.argv[3]) if len(sys.argv) > 3 else 2
primes = poisson.PRIMES[:nprimes]
phi6 = json.load(open("out/phi_H6.json"))["coeffs_low_to_high"]
if json.load(open(f"{outdir}/phi_H6.json"))["coeffs_low_to_high"] != phi6:
    raise RuntimeError('H6 input mismatch')
if len(primes) != nprimes or math.prod(primes) <= 2*4**448:
    raise RuntimeError('Insufficient prime product for certified H7 lift')
logf = open(f"{outdir}/h7_log.txt", "a")
def log(s):
    print(s, flush=True); logf.write(s + "\n"); logf.flush()
log(f"=== H_7 with {nprimes} primes, {nproc} processes, {time.ctime()}")
per_prime = {}
with Pool(nproc) as pool:
    for r in pool.imap_unordered(poisson.work, [(7, p, phi6) for p in primes]):
        if not r['check_ok'] or r['poly'][-1] != 1:
            raise RuntimeError('Interpolation or monicity failure')
        per_prime[r["p"]] = r["poly"]
        log(f"   p={r['p']}: ok, {r['n_extra_checks']} extra checks, skipped {[s[0] for s in r['skipped']]}, {r['time']:.1f}s")
        json.dump(per_prime, open(f"{outdir}/h7_per_prime.json", "w"))
phi = poisson.poly_lift(per_prime, primes)
M = math.prod(primes)
log(f"   modulus bits = {M.bit_length()}  (log2 M = {math.log2(M):.2f}); max coefficient bits = {max(abs(c).bit_length() for c in phi)}")
log(f"   lift stable dropping 1 prime: {poisson.poly_lift(per_prime, primes[:-1]) == phi}; dropping 2: {poisson.poly_lift(per_prime, primes[:-2]) == phi}")
phi12 = json.load(open("out/phi_H7.json"))["coeffs_low_to_high"]
log(f"   identical to the 12-prime result: {phi == phi12}")
json.dump({"m": 7, "degree": 448, "coeffs_low_to_high": phi, "primes": primes, "modulus_bits": M.bit_length(),
           "identical_to_12_prime_run": phi == phi12}, open(f"{outdir}/phi_H7.json", "w"))
log(f"=== finished {time.ctime()}")
