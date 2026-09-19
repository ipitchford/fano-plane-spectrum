#!/usr/bin/env python3
"""Different determinant construction of phi_F mod p, sharing interpolation helpers
with Poisson. No Poisson formula or Singular in determinant evaluation."""
import json, sys, time
from multiprocessing import Pool
from macaulay import macaulay_value, edges_induced
from poisson import interpolate_mod_p, evalpoly

p = int(sys.argv[1]) if len(sys.argv) > 1 else 2147483647
nproc = int(sys.argv[2]) if len(sys.argv) > 2 else 2
edges = edges_induced(7)

def ev(lam0):
    t = time.time()
    val, dM, dMp = macaulay_value(7, lam0, edges, p)
    return lam0, val, dMp, time.time() - t

if __name__ == "__main__":
    lams = list(range(1, 453))
    log = open(f"out/macaulay_full_p{p}_log.txt", "a")
    pts = []
    with Pool(nproc) as pool:
        for lam0, val, dMp, dt in pool.imap_unordered(ev, lams):
            if val is None:
                log.write(f"lambda0={lam0}: det M' = 0 mod p, skipped\n"); log.flush(); continue
            pts.append((lam0, val))
            log.write(f"lambda0={lam0}: phi={val} ({dt:.1f}s)\n"); log.flush()
    pts.sort()
    if len(pts) < 450:
        raise RuntimeError('Need 449 interpolation points and a surplus check')
    poly = interpolate_mod_p(pts[:449], p)
    extra_ok = all(evalpoly(poly, x, p) == y for x, y in pts[449:])
    ref = json.load(open("out/phi_H7.json"))["coeffs_low_to_high"]
    same = [c % p for c in ref] == poly
    if not extra_ok or not same or len(poly) != 449 or poly[-1] != 1:
        raise RuntimeError('Macaulay interpolation or comparison failed')
    res = {"p": p, "n_points": len(pts), "interpolation_extra_checks_ok": extra_ok,
           "identical_to_poisson_result_mod_p": same, "n_coefficients_differing": sum(1 for a, b in zip(poly, ref) if a != b % p)}
    log.write(json.dumps(res) + "\n")
    json.dump({**res, "poly_mod_p": poly}, open(f"out/macaulay_full_p{p}.json", "w"))
    print(json.dumps(res))
