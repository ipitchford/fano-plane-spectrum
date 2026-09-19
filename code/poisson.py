#!/usr/bin/env python3
"""
Characteristic polynomial of the Fano plane (3-uniform hypergraph, 7 vertices, 7 edges)
via the Poisson product formula for resultants (Cox, Little & O'Shea, Using Algebraic Geometry,
Ch. 3 Sec. 3, Thm 3.4), in the normalisation of Cooper & Dutle (2012):

    (A x^{2})_i = sum_{edges e containing i} prod_{j in e, j != i} x_j,
    phi_H(lambda) = Res( lambda x_i^2 - (A x^2)_i , i = 1..n ),  deg phi_H = n 2^{n-1}.

Order the vertices 1..n and let H_m be the induced sub-hypergraph on {1..m}.  Writing
F_i^{(m)} for the forms of H_m, the Poisson formula (dehomogenising at x_m = 1) gives, for every
lambda_0 with phi_{H_{m-1}}(lambda_0) != 0,

    phi_{H_m}(lambda_0) = phi_{H_{m-1}}(lambda_0)^2 * det( m_f ),

    m_f = multiplication by f = lambda_0 - F_m^{(m)}(x_1..x_{m-1},1) on the algebra
          k[x_1..x_{m-1}] / < lambda_0 x_i^2 - F_i^{(m)}(x_1..x_{m-1},1) : i < m >   (dim 2^{m-1}).

phi_{H_m} is a monic integer polynomial of degree m 2^{m-1}; we evaluate the right-hand side
modulo many 31-bit primes at deg+4 integer points lambda_0 (Singular: std, kbase, reduce, det),
interpolate over F_p, lift by CRT, and check stability of the lift when primes are dropped.
"""
import subprocess, sys, os, json, time, math
from sympy import isprime
from multiprocessing import Pool

LINES = [(1,2,4),(2,3,5),(3,4,6),(4,5,7),(5,6,1),(6,7,2),(7,1,3)]
if os.environ.get("EDGES"):
    LINES = [tuple(e) for e in json.loads(os.environ["EDGES"])]
NV = int(os.environ.get("NV", "7"))
SINGULAR = "Singular"

def edges_induced(m):
    return [tuple(sorted(e)) for e in LINES if max(e) <= m]

def F_poly(i, m):
    """F_i(x_1..x_{m-1}, x_m = 1) for H_m as a Singular expression."""
    terms = []
    for e in edges_induced(m):
        if i in e:
            others = [j for j in e if j != i]
            factors = ["1" if j == m else f"x{j}" for j in others]
            terms.append("*".join(factors))
    return "+".join(terms) if terms else "0"

def singular_script(m, p, lams):
    nv = m - 1
    lines = [f"ring r = {p}, ({','.join('x%d'%i for i in range(1,nv+1)) if nv>0 else 'x1'}), dp;",
             "option(redSB);"]
    for lam in lams:
        lines.append(f"int lam = {lam};")
        if nv == 0:
            lines.append(f"printf(\"RES %s %s %s\", {lam}, 1, lam);")
            lines.append("kill lam;")
            continue
        gens = [f"lam*x{i}^2 - ({F_poly(i, m)})" for i in range(1, m)]
        lines += [f"ideal I = {','.join(gens)};",
                  "ideal G = std(I);",
                  "int vd = vdim(G);",
                  f"poly f = lam - ({F_poly(m, m)});",
                  "ideal B = kbase(G);",
                  "int nb = size(B);",
                  "matrix M[nb][nb];",
                  "int a; int b; poly g; int k;",
                  "for (a=1; a<=nb; a++) {",
                  "  g = reduce(f*B[a], G);",
                  "  for (k=1; k<=size(g); k++) {",
                  "    for (b=1; b<=nb; b++) {",
                  "      if (leadmonom(g[k]) == B[b]) { M[b,a] = leadcoef(g[k]); }",
                  "    }",
                  "  }",
                  "}",
                  "poly d = det(M);",
                  f"printf(\"RES %s %s %s\", {lam}, vd, leadcoef(d));",
                  "kill I, G, vd, f, B, nb, M, a, b, g, k, d, lam;"]
    lines.append("quit;")
    return "\n".join(lines)

def run_singular(script, p):
    r = subprocess.run([SINGULAR, "-q", "--no-warn", "--no-out"], input=script, capture_output=True, text=True)
    if r.returncode != 0 or '?' in r.stdout:
        raise RuntimeError("Singular failed:\n" + r.stderr + "\n" + r.stdout[-2000:])
    res = {}
    for line in r.stdout.splitlines():
        if line.startswith("RES "):
            _, lam, vd, d = line.split()
            res[int(lam)] = (int(vd), int(d) % p)
    return res

def interpolate_mod_p(points, p):
    """Newton interpolation over F_p; returns coefficients low->high."""
    n = len(points)
    xs = [x % p for x, _ in points]
    coef = [y % p for _, y in points]
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) * pow((xs[i] - xs[i - j]) % p, p - 2, p) % p
    poly = [coef[n - 1]]
    for i in range(n - 2, -1, -1):
        newp = [0] * (len(poly) + 1)
        for k, c in enumerate(poly):
            newp[k + 1] = (newp[k + 1] + c) % p
            newp[k] = (newp[k] - xs[i] * c) % p
        newp[0] = (newp[0] + coef[i]) % p
        poly = newp
    return poly

def evalpoly(poly, x, p):
    v = 0
    for c in reversed(poly):
        v = (v * x + c) % p
    return v

def crt_pair(r1, m1, r2, m2):
    t = ((r2 - r1) * pow(m1, -1, m2)) % m2
    return (r1 + m1 * t) % (m1 * m2), m1 * m2

def symmetric(r, m):
    return r - m if r > m // 2 else r

def work(args):
    """Compute phi_{H_m} mod p by interpolation. args = (m, p, phi_prev (int coeffs))."""
    m, p, phi_prev = args
    deg = m * 2 ** (m - 1)
    lams = list(range(1, deg + 5))
    t0 = time.time()
    res = run_singular(singular_script(m, p, lams), p)
    pts, skipped = [], []
    for lam in lams:
        prev = evalpoly(phi_prev, lam, p)
        vd, d = res[lam]
        if prev == 0:
            skipped.append((lam, prev, vd))
            continue
        if m > 1 and vd != 2 ** (m - 1):
            raise RuntimeError(f'Unexpected quotient dimension {vd} at m={m}, p={p}, lambda={lam}')
        pts.append((lam, prev * prev % p * d % p))
    if len(pts) < deg + 2:
        raise RuntimeError(f"m={m} p={p}: only {len(pts)} usable points")
    poly = interpolate_mod_p(pts[:deg + 1], p)
    ok = all(evalpoly(poly, x, p) == y for x, y in pts[deg + 1:])
    return {"m": m, "p": p, "poly": poly, "check_ok": ok, "n_extra_checks": len(pts) - deg - 1,
            "skipped": skipped, "time": time.time() - t0}

def poly_lift(per_prime, primes):
    deg = len(per_prime[primes[0]]) - 1
    out = []
    for k in range(deg + 1):
        r, M = per_prime[primes[0]][k], primes[0]
        for p in primes[1:]:
            r, M = crt_pair(r, M, per_prime[p][k], p)
        out.append(symmetric(r, M))
    return out

PRIMES = [2147483647, 2147483629, 2147483587, 2147483579, 2147483563, 2147483549, 2147483543, 2147483497,
          2147483489, 2147483477, 2147483423, 2147483399, 2147483353, 2147483323, 2147483269, 2147483249,
          2147483237, 2147483179, 2147483171, 2147483137, 2147483123, 2147483077, 2147483069, 2147483059,
          2147483053, 2147483033, 2147483029, 2147482951, 2147482949, 2147482943, 2147482937, 2147482921,
          2147482883, 2147482861, 2147482819, 2147482817, 2147482811, 2147482801, 2147482763, 2147482739,
          2147482697, 2147482693, 2147482681, 2147482663, 2147482661, 2147482621, 2147482591, 2147482583]

def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else "out"
    nprimes = int(sys.argv[2]) if len(sys.argv) > 2 else 32
    nproc = int(sys.argv[3]) if len(sys.argv) > 3 else 2
    os.makedirs(outdir, exist_ok=True)
    logf = open(os.path.join(outdir, "poisson_log.txt"), "a")
    def log(s):
        print(s, flush=True); logf.write(s + "\n"); logf.flush()
    primes = PRIMES[:nprimes]
    if len(primes) != nprimes or nprimes < 3 or len(set(primes)) != nprimes or not all(isprime(p) for p in primes):
        raise ValueError('Need 3..48 distinct supported primes')
    log(f"=== Poisson recursion for the Fano plane: {len(primes)} primes, {nproc} processes, {time.ctime()}")
    phi_prev = [1]  # phi of the empty hypergraph on 0 vertices
    for m in range(1, NV + 1):
        deg = m * 2 ** (m - 1)
        log(f"-- H_{m}: edges {edges_induced(m)}, deg phi = {deg}")
        with Pool(nproc) as pool:
            results = pool.map(work, [(m, p, phi_prev) for p in primes])
        per_prime = {}
        for r in results:
            if not r['check_ok'] or r['poly'][-1] != 1:
                raise RuntimeError(f'Interpolation or monicity failure m={m} p={r["p"]}')
            per_prime[r["p"]] = r["poly"]
            log(f"   p={r['p']}: ok, {r['n_extra_checks']} extra checks, skipped {[(s[0]) for s in r['skipped']]}, {r['time']:.1f}s")
        phi = poly_lift(per_prime, primes)
        # stability: drop last 1 and last 2 primes
        stable1 = poly_lift(per_prime, primes[:-1]) == phi
        stable2 = poly_lift(per_prime, primes[:-2]) == phi if len(primes) > 2 else None
        maxbits = max(abs(c).bit_length() for c in phi)
        log(f"   lift: max coefficient bits = {maxbits} (modulus bits = {sum(p.bit_length() for p in primes)}); stable dropping 1 prime: {stable1}; dropping 2: {stable2}")
        if not (stable1 and stable2):
            raise RuntimeError('Unstable CRT lift: increase prime count')
        delta = max(sum(i in e for e in edges_induced(m)) for i in range(1,m+1))
        if math.prod(primes) <= 2*(1+delta)**deg:
            raise RuntimeError('Insufficient a-priori CRT bound: increase prime count')
        json.dump({"m": m, "edges": edges_induced(m), "degree": deg, "coeffs_low_to_high": phi,
                   "primes": primes, "stable_drop1": stable1, "stable_drop2": stable2},
                  open(os.path.join(outdir, f"phi_H{m}.json"), "w"))
        phi_prev = phi
    log(f"=== finished {time.ctime()}")
    phi = phi_prev
    deg = len(phi) - 1
    log(f"codegree coefficients c_d (coefficient of lambda^({deg}-d)) for d = 0..16:")
    for d in range(17):
        log(f"   c_{d} = {phi[deg - d]}")

if __name__ == "__main__":
    main()
