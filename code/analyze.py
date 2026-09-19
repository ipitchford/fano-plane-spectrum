#!/usr/bin/env python3
"""Factor the characteristic polynomial of the Fano plane and describe its spectrum."""
import json, sys
from flint import fmpz_poly, fmpq_poly, arb_poly, acb_poly, ctx, fmpz
ctx.dps = 60

outdir = sys.argv[1] if len(sys.argv) > 1 else "out"
d = json.load(open(f"{outdir}/phi_H7.json"))
coeffs = d["coeffs_low_to_high"]
phi = fmpz_poly(coeffs)
deg = phi.degree()
print("degree", deg, "monic", coeffs[-1] == 1)
print("max |coefficient| bits", max(abs(c).bit_length() for c in coeffs))

# Clark-Cooper (LAA 649, 2022, Fig. 2) leading coefficients of the Fano plane
cc = {0:1,1:0,2:0,3:-336,4:0,5:0,6:55524,7:-696,8:0,9:-6017746,10:220038,11:0,12:481293561,13:-34237560,14:-122004,15:-30303162330}
print("Clark-Cooper comparison:")
allok = True
for k, v in cc.items():
    mine = coeffs[deg - k]
    ok = mine == v
    allok &= ok
    print(f"  c_{k:2d}: ours {mine}  Clark-Cooper {v}  {'OK' if ok else 'MISMATCH'}")
print("all 16 leading coefficients agree:", allok)

# factorisation over Z
c, fac = phi.factor()
print("content", c)
fac = sorted(fac, key=lambda t: (t[0].degree(), str(t[0])))
tot = 0
for f, e in fac:
    tot += f.degree() * e
    print(f"  [{f}]^{e}   (degree {f.degree()})")
print("sum of degree*mult =", tot)
json.dump({"content": int(c), "factors": [{"coeffs_low_to_high": [int(x) for x in f.coeffs()], "mult": int(e)} for f, e in fac]},
          open(f"{outdir}/factorisation.json", "w"), indent=1)

# roots of each factor (complex), with multiplicity
print("\nDistinct eigenvalues (roots of irreducible factors) with algebraic multiplicities:")
rows = []
for f, e in fac:
    p = acb_poly([complex(int(x)) for x in f.coeffs()])
    # use arbitrary precision root finding
    pa = acb_poly([int(x) for x in f.coeffs()])
    roots = pa.roots()
    for r in roots:
        rows.append((f, e, r))
rows.sort(key=lambda t: (-t[2].real.mid() if hasattr(t[2].real,'mid') else 0))
for f, e, r in rows:
    print(f"  {r}   mult {e}   (factor degree {f.degree()})")
