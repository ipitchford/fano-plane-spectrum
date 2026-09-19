import subprocess, json, itertools
LINES = [(1,2,4),(2,3,5),(3,4,6),(4,5,7),(5,6,1),(6,7,2),(7,1,3)]
V = list(range(1,8))
reps = {
 "T1 point-transitive (|G|=168)": ((1,2,3,4,5,6,7),),
 "T2 point stabiliser (24)": ((1,),(2,3,4,5,6,7)),
 "T3 line stabiliser (24)": ((1,2,4),(3,5,6,7)),
 "T4 flag stabiliser (8)": ((1,),(5,6),(2,3,4,7)),
 "T5 antiflag stabiliser (6)": ((1,),(2,3,5),(4,6,7)),
 "T6 two-point stabiliser (4)": ((1,),(2,),(4,),(3,5,6,7)),
 "T7 Klein-type (4)": ((1,),(2,4),(3,7),(5,6)),
 "T8 involution (2)": ((1,),(2,),(4,),(3,5),(6,7)),

}
out = {}
for name, P in reps.items():
    r = len(P)
    part_of = {v: k for k, p in enumerate(P) for v in p}
    found = {}
    for k in range(r):
        avars = [f"a{j}" for j in range(r) if j != k]
        def xv(v):
            j = part_of[v]; return "1" if j == k else f"a{j}"
        eqs = []
        for i in V:
            terms = []
            for l in LINES:
                if i in l:
                    j, kk = sorted(set(l) - {i}); terms.append(f"{xv(j)}*{xv(kk)}")
            eqs.append(f"{'+'.join(terms)} - lam*({xv(i)})^2")
        ring_vars = ",".join(avars + ["lam"])
        script = f"""LIB "elim.lib";
ring r = 0, ({ring_vars}), dp;
ideal I = {",".join(eqs)};
ideal J = std(I);
if (dim(J) == -1) {{ printf("ELIM EMPTY"); }} else {{
ideal E = eliminate(J, {"*".join(avars) if avars else "1"});
poly e = E[1];
printf("ELIM %s", factorize(e));
}}
quit;
"""
        try:
            rr = subprocess.run(["Singular","-q","--no-warn"], input=script, capture_output=True, text=True, timeout=1500)
        except subprocess.TimeoutExpired:
            found[f"normalise part {P[k]} = 1"] = "TIMEOUT"; continue
        line = [l for l in rr.stdout.splitlines() if l.startswith("ELIM")]
        found[f"normalise part {P[k]} = 1"] = line[0] if line else rr.stdout[-300:]
    out[name] = {"partition": P, "results": found}
    print(name, P)
    for kk, v in found.items(): print("   ", kk, "->", v)
json.dump(out, open("out/symmetric_eigenvectors.json","w"), indent=1)
