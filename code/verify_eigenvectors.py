#!/usr/bin/env python3
"""
Symbolic verification of explicit eigenvectors for every distinct eigenvalue of the Fano plane.
Each eigenvector is given as a vector of rational functions in lam (and, for two families, in a
cube root of unity w with w^2 + w + 1 = 0).  We check that F_i(x) - lam * x_i^2 reduces to 0
modulo the minimal polynomial of lam (and w^2 + w + 1 where relevant) for all i.
"""
from sympy import symbols, Poly, together, fraction, factor, expand, sqrt, I, nsimplify, Rational, N, QQ
from sympy import rem, resultant, gcd

lam, w = symbols('lam w')
LINES = [(1,2,4),(2,3,5),(3,4,6),(4,5,7),(5,6,1),(6,7,2),(7,1,3)]
V = range(1, 8)

def F(x, i):
    return sum(x[j]*x[k] for l in LINES if i in l for (j, k) in [tuple(sorted(set(l) - {i}))])

def check(name, minpoly, x, use_w=False):
    """x: dict vertex->expression. Verify F_i(x) = lam x_i^2 modulo minpoly (and w^2+w+1)."""
    ok = True
    if not any(value == 1 for value in x.values()):
        raise ValueError('Expected a unit coordinate certifying a nonzero vector')
    for value in x.values():
        den = fraction(together(value))[1]
        if w in den.free_symbols or gcd(Poly(den, lam), Poly(minpoly, lam)).degree() != 0:
            raise ValueError('Denominator is not certified nonvanishing')
    for i in V:
        expr = together(F(x, i) - lam*x[i]**2)
        num, den = fraction(expr)
        num = expand(num)
        # reduce modulo w^2+w+1 first (if present), then modulo minpoly in lam
        if use_w:
            num = rem(Poly(num, w), Poly(w**2 + w + 1, w)).as_expr()
            num = expand(num)
        r = rem(Poly(num, lam), Poly(minpoly, lam)) if num != 0 else 0
        if use_w and r != 0:
            # residue may still involve w; reduce again coefficient-wise
            r = expand(rem(Poly(expand(r.as_expr()), w), Poly(w**2 + w + 1, w)).as_expr())
            if r != 0:
                r = rem(Poly(r, lam), Poly(minpoly, lam))
        if r != 0 and getattr(r, 'is_zero', None) is not True:
            ok = False
            print(f"   vertex {i}: residue {r}")
    print(f"{'OK ' if ok else 'FAIL'}  {name}: minimal polynomial {minpoly}")
    return ok

results = []
# 1. lambda = 3, all-ones
results.append(check("lambda=3, x = (1,...,1)", lam - 3, {i: 1 for i in V}))
# 2. lambda = 0, x = e_1
results.append(check("lambda=0, x = e_1", lam, {i: (1 if i == 1 else 0) for i in V}))
# 3. lambda = 1, indicator of line {1,2,4}
results.append(check("lambda=1, x = 1_{124}", lam - 1, {i: (1 if i in (1,2,4) else 0) for i in V}))
# 4. lambda = w (w^2+w+1=0): x = (1, w, 0, 1, 0, 0, 0) on line {1,2,4}
results.append(check("lambda=w (w^2+w+1=0), x=(1,w,0,1,0,0,0)", lam**2 + lam + 1,
                     {1: 1, 2: lam, 3: 0, 4: 1, 5: 0, 6: 0, 7: 0}))
# 5. lambda^2 - lambda + 1 = 0: x = all ones except x_1 = lambda - 2
results.append(check("lambda^2-lambda+1=0, x = 1 + (lambda-3) e_1", lam**2 - lam + 1,
                     {i: (lam - 2 if i == 1 else 1) for i in V}))
# 6. lambda^2 + 2 lambda + 6 = 0: x = lambda/3 on line {1,2,4}, 1 elsewhere
results.append(check("lambda^2+2lambda+6=0, x = lambda/3 on {1,2,4}, 1 elsewhere", lam**2 + 2*lam + 6,
                     {i: (lam/3 if i in (1,2,4) else 1) for i in V}))
# 7. point p=2, line M={4,5,7} not through p. Lines through 2: {2,6,7} (v=7,u=6), {2,3,5} (v=5,u=3), {1,2,4} (v=4,u=1)
#    x_p = 0, x_v = zeta_L, x_u = mu zeta_L, zeta = 1, w, w^2 ; mu = 2/lambda ; (lambda-2)(lambda^2+lambda+2)=0
def pl_vec(mu):
    return {2: 0, 7: 1, 6: mu, 5: w, 3: mu*w, 4: w**2, 1: mu*w**2}
results.append(check("lambda=2, x_p=0, x_v=zeta_L, x_u=zeta_L (cube roots of unity on the lines through p)", lam - 2, pl_vec(1), use_w=True))
results.append(check("lambda^2+lambda+2=0, x_p=0, x_v=zeta_L, x_u=(2/lambda) zeta_L", lam**2 + lam + 2, pl_vec(2/lam), use_w=True))
# 8. cubic: flag p=2 on L={2,6,7}: x_2 = (lam^2+2lam+4)/(lam+2), x_6 = x_7 = -2/(lam+2), x = 1 off L
results.append(check("lambda^3+2lambda^2+2lambda-2=0 (flag ansatz)", lam**3 + 2*lam**2 + 2*lam - 2,
                     {2: (lam**2 + 2*lam + 4)/(lam + 2), 6: -2/(lam + 2), 7: -2/(lam + 2), 1: 1, 3: 1, 4: 1, 5: 1}))
# 9. quartic: antiflag p=1, M={2,3,5}: x_1 = -(lam+1)(lam^2-2lam+2), x = lam^2-1 on M, 1 on {4,6,7}
results.append(check("lambda^4-lambda^3-lambda^2+lambda+1=0 (antiflag ansatz)", lam**4 - lam**3 - lam**2 + lam + 1,
                     {1: -(lam + 1)*(lam**2 - 2*lam + 2), 2: lam**2 - 1, 3: lam**2 - 1, 5: lam**2 - 1, 4: 1, 6: 1, 7: 1}))
print("ALL OK" if all(results) else "SOME FAILED")
if not all(results):
    raise SystemExit(1)
