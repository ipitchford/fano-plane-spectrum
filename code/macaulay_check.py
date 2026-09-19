import json, time, random, sys
from macaulay import macaulay_value, edges_induced
d = json.load(open("out/phi_H7.json")); coeffs = d["coeffs_low_to_high"]
def evalpoly(poly, x, p):
    v = 0
    for c in reversed(poly): v = (v * x + c) % p
    return v
seed = int(sys.argv[1]); ntr = int(sys.argv[2]); p = int(sys.argv[3])
random.seed(seed)
edges = edges_induced(7)
results = []
for trial in range(ntr):
    lam0 = random.randrange(2, p)
    t = time.time()
    val, dM, dMp = macaulay_value(7, lam0, edges, p)
    pv = evalpoly(coeffs, lam0, p)
    res = {"p": p, "lambda0": lam0, "macaulay_phi_mod_p": val, "poisson_phi_mod_p": pv, "agree": val == pv, "detM": dM, "detMprime": dMp, "seconds": round(time.time()-t,1)}
    print(json.dumps(res), flush=True)
    results.append(res)
json.dump(results, open(f"out/macaulay_check_p{p}_seed{seed}.json", "w"), indent=1)
