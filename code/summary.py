#!/usr/bin/env python3
"""Produce the final summary tables / JSON for the Fano plane spectrum."""
import json, sys
from flint import fmpz_poly, acb_poly, arb, ctx
ctx.dps = 50
outdir = sys.argv[1] if len(sys.argv) > 1 else "out"
d = json.load(open(f"{outdir}/phi_H7.json"))
coeffs = d["coeffs_low_to_high"]
phi = fmpz_poly(coeffs)
deg = phi.degree()
c, fac = phi.factor()
if c != 1:
    raise RuntimeError('Nonmonic factorization')
fac = sorted(fac, key=lambda t: (t[0].degree(), str(t[0])))
prod = fmpz_poly([1])
for f, e in fac:
    prod *= f ** e
if prod != phi:
    raise RuntimeError('Factorization does not multiply back')

# eigenvector descriptions (see verify_eigenvectors.py)
desc = {
 "x": ("0", "e_p (a single vertex); also many +-1 vectors", True),
 "x + (-1)": ("1", "indicator vector of a line", True),
 "x + (-2)": ("2", "x_p = 0; on the three lines through p the two other points carry a common cube root of unity zeta_L, distinct for the three lines (no real eigenvector)", False),
 "x + (-3)": ("3", "all-ones vector (Perron vector)", True),
 "x^2 + (-1)*x + 1": ("(1 +- i sqrt3)/2", "all-ones except x_p = lambda - 2", False),
 "x^2 + 2*x + 6": ("-1 +- i sqrt5", "lambda/3 on a line, 1 elsewhere", False),
 "x^2 + x + 1": ("(-1 +- i sqrt3)/2", "(1, lambda, 1) on a line, 0 elsewhere", False),
 "x^2 + x + 2": ("(-1 +- i sqrt7)/2", "x_p = 0; x_v = zeta_L, x_u = (2/lambda) zeta_L on each line {p,u,v} through p, where the v's form a line", False),
 "x^3 + 2*x^2 + 2*x + (-2)": ("real root 0.5747..., and a complex pair", "flag (p in L): x_p = (lambda^2+2lambda+4)/(lambda+2), x = -2/(lambda+2) on L minus p, 1 off L", None),
 "x^4 + (-1)*x^3 + (-1)*x^2 + x + 1": ("two complex pairs", "antiflag (p not on M): x_p = -(lambda+1)(lambda^2-2lambda+2), x = lambda^2-1 on M, 1 on the other three points", False),
}
rows = []
for f, e in fac:
    pa = acb_poly([int(x) for x in f.coeffs()])
    roots = pa.roots()
    for r in roots:
        re, im = r.real, r.imag
        isreal = im.contains(0) and f.degree() == 1 or (f.degree() == 3 and abs(float(im.mid())) < 1e-30)
        rows.append({"factor": str(f), "factor_degree": f.degree(), "algebraic_multiplicity": int(e),
                     "eigenvalue_re": str(re.mid().str(30, radius=False)), "eigenvalue_im": str(im.mid().str(30, radius=False)),
                     "modulus": str(abs(r).mid().str(20, radius=False)),
                     "real": bool(isreal)})
rows.sort(key=lambda t: (-float(t["eigenvalue_re"]), float(t["eigenvalue_im"])))
summary = {
 "hypergraph": "Fano plane PG(2,2) as a 3-uniform hypergraph; vertices 1..7, lines 124 235 346 457 156 267 137",
 "normalisation": "Cooper-Dutle: a_{ijk} = 1/2 on lines; (A x^2)_i = sum over lines {i,j,k} of x_j x_k; eigenvalue equation A x^2 = lambda x^[2]",
 "characteristic_polynomial_degree": deg,
 "max_abs_coefficient_bits": max(abs(x).bit_length() for x in coeffs),
 "factorisation": [{"factor": str(f), "multiplicity": int(e)} for f, e in fac],
 "number_of_distinct_eigenvalues": sum(f.degree() for f, e in fac),
 "spectral_radius": 3, "spectral_radius_multiplicity": 1,
 "zero_multiplicity": int([e for f, e in fac if str(f) == "x"][0]),
 "real_eigenvalues": ["0", "1", "2", "3", "0.5747430735... (real root of x^3+2x^2+2x-2)"],
 "H_eigenvalues (real with a real eigenvector)": ["0", "1", "3", "0.5747430735..."],
 "real_eigenvalue_without_real_eigenvector": ["2"],
 "eigenvalues": rows,
 "eigenvector_descriptions": {k: {"values": v[0], "eigenvector": v[1]} for k, v in desc.items()},
 "coefficients_low_to_high": coeffs,
}
json.dump(summary, open(f"{outdir}/fano_spectrum_summary.json", "w"), indent=1)

# human-readable table
with open(f"{outdir}/fano_spectrum_table.md", "w") as fh:
    fh.write("| eigenvalue (numerical) | modulus | minimal polynomial | alg. multiplicity |\n|---|---|---|---|\n")
    for r in rows:
        re, im = float(r["eigenvalue_re"]), float(r["eigenvalue_im"])
        s = f"{re:.10f}" + (f" {'+' if im>=0 else '-'} {abs(im):.10f} i" if abs(im) > 1e-20 else "")
        fh.write(f"| {s} | {float(r['modulus']):.6f} | {r['factor'].replace('x','λ')} | {r['algebraic_multiplicity']} |\n")
    tot = sum(r["algebraic_multiplicity"] for r in rows)
    fh.write(f"\nTotal multiplicity: {tot} (= 7 * 2^6 = 448)\n")
print(open(f"{outdir}/fano_spectrum_table.md").read())

# polynomial as text, both orders
with open(f"{outdir}/fano_charpoly_coefficients.txt", "w") as fh:
    fh.write("# Characteristic polynomial of the Fano plane (Cooper-Dutle normalisation), degree 448.\n")
    fh.write("# Line k: coefficient of lambda^k, k = 0..448.\n")
    for k, ck in enumerate(coeffs):
        fh.write(f"{k} {ck}\n")
with open(f"{outdir}/fano_charpoly_factored.txt", "w") as fh:
    fh.write(" * ".join(f"({str(f).replace('x','L')})^{e}" for f, e in fac) + "\n")
