import subprocess, json
LINES = [(1,2,4),(2,3,5),(3,4,6),(4,5,7),(5,6,1),(6,7,2),(7,1,3)]
V = list(range(1,8))
P = ((1,),(2,),(4,),(3,5),(6,7))   # orbits of the involution fixing line {1,2,4}
names = ["a","b","c","d","e"]
part_of = {v: k for k, p in enumerate(P) for v in p}
factors = {"t":"t","t-1":"t-1","t-2":"t-2","t-3":"t-3","t2-t+1":"t^2-t+1","t2+2t+6":"t^2+2*t+6","t2+t+1":"t^2+t+1",
           "t2+t+2":"t^2+t+2","t3+2t2+2t-2":"t^3+2*t^2+2*t-2","t4-t3-t2+t+1":"t^4-t^3-t^2+t+1"}
out = {}
for name, g in factors.items():
    out[name] = {}
    for k in range(5):
        def xv(v):
            j = part_of[v]; return "1" if j == k else names[j]
        eqs = []
        for i in V:
            terms = []
            for l in LINES:
                if i in l:
                    j, kk = sorted(set(l) - {i}); terms.append(f"{xv(j)}*{xv(kk)}")
            eqs.append(f"{'+'.join(terms)} - lam*({xv(i)})^2")
        vars_ = [names[j] for j in range(5) if j != k]
        lin = g in ("t","t-1","t-2","t-3")
        if lin:
            val = {"t":"0","t-1":"1","t-2":"2","t-3":"3"}[g]
            ring = f"ring r = 0, ({','.join(vars_)}), lp;"
            eqs = [e.replace("lam", f"({val})") for e in eqs]
        else:
            ring = f"ring r = (0,t), ({','.join(vars_)}), lp; minpoly = {g};"
            eqs = [e.replace("lam", "t") for e in eqs]
        script = f"""LIB "primdec.lib";
{ring}
ideal I = {",".join(eqs)};
ideal G = std(I);
if (dim(G) == -1) {{ printf("NOSOL"); }} else {{
list L = primdecGTZ(I);
int i;
for (i=1; i<=size(L); i++) {{ ideal Q = std(L[i][2]); printf("COMPONENT dim %s vdim %s", dim(Q), vdim(Q)); Q; }}
}}
quit;
"""
        rr = subprocess.run(["Singular","-q","--no-warn"], input=script, capture_output=True, text=True, timeout=600)
        out[name][f"{names[k]}=1"] = rr.stdout.strip()
        print(f"### factor {g}, normalisation {names[k]}=1  (x1=a, x2=b, x4=c, x3=x5=d, x6=x7=e)")
        print(rr.stdout.strip())
json.dump(out, open("out/explicit_eigenvectors_involution_ansatz.json","w"), indent=1)
