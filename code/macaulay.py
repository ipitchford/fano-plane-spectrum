#!/usr/bin/env python3
"""
Independent check: evaluate the characteristic polynomial phi_H(lambda_0) modulo a prime p
using Macaulay's resultant formula  Res = det(M) / det(M')  for the system
    P_i = lambda_0 x_i^2 - F_i(x),  i = 1..n,
where M is the Macaulay matrix in degree D = n+1 (quadrics: sum (d_i - 1) + 1) and M' is the
submatrix indexed by monomials divisible by x_i^2 for at least two indices i.
(Macaulay 1902; Cox-Little-O'Shea, Using Algebraic Geometry, Ch. 3 Thm 4.9.)  The identity
det M = Res * det M' holds as polynomials in the coefficients, hence for any specialisation;
it determines Res whenever det M' != 0.  Used only for spot checks of the Poisson computation.
"""
import sys, itertools, json
from flint import nmod_mat

LINES = [(1,2,4),(2,3,5),(3,4,6),(4,5,7),(5,6,1),(6,7,2),(7,1,3)]

def monomials(n, D):
    """All exponent vectors of degree D in n variables."""
    if n == 1:
        yield (D,); return
    for a in range(D, -1, -1):
        for rest in monomials(n - 1, D - a):
            yield (a,) + rest

def forms(n, lam0, edges):
    """P_i as dict exponent->coeff (integers), i = 1..n, for hypergraph on vertices 1..n."""
    P = []
    for i in range(1, n + 1):
        d = {}
        e_i = [0] * n; e_i[i - 1] = 2
        d[tuple(e_i)] = lam0
        for e in edges:
            if i in e:
                ex = [0] * n
                for j in e:
                    if j != i: ex[j - 1] += 1
                d[tuple(ex)] = d.get(tuple(ex), 0) - 1
        P.append(d)
    return P

def macaulay_value(n, lam0, edges, p):
    D = n + 1  # sum(d_i - 1) + 1 with all d_i = 2
    mons = list(monomials(n, D))
    idx = {m: k for k, m in enumerate(mons)}
    P = forms(n, lam0, edges)
    N = len(mons)
    M = nmod_mat(N, N, p)
    reduced2 = []  # rows/cols indexed by monomials with >=2 exponents >= 2
    for r, alpha in enumerate(mons):
        # assign to smallest i with alpha_i >= 2
        i = next(k for k in range(n) if alpha[k] >= 2)
        big = sum(1 for k in range(n) if alpha[k] >= 2)
        if big >= 2: reduced2.append(r)
        beta = list(alpha); beta[i] -= 2  # multiplier monomial x^beta
        for ex, c in P[i].items():
            gamma = tuple(beta[k] + ex[k] for k in range(n))
            M[r, idx[gamma]] = (int(M[r, idx[gamma]]) + c) % p
    detM = int(M.det())
    # M' : rows and columns in reduced2
    k = len(reduced2)
    Mp = nmod_mat(k, k, p)
    for a, r in enumerate(reduced2):
        for b, c in enumerate(reduced2):
            Mp[a, b] = M[r, c]
    detMp = int(Mp.det())
    if detMp == 0:
        return None, detM, detMp
    return detM * pow(detMp, p - 2, p) % p, detM, detMp

def edges_induced(m):
    return [tuple(sorted(e)) for e in LINES if max(e) <= m]

if __name__ == "__main__":
    m = int(sys.argv[1]); lam0 = int(sys.argv[2]); p = int(sys.argv[3])
    edges = edges_induced(m)
    val, dM, dMp = macaulay_value(m, lam0, edges, p)
    print(json.dumps({"m": m, "lambda0": lam0, "p": p, "phi_mod_p": val, "detM": dM, "detMprime": dMp}))
