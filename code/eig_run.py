import subprocess, sys
factors = {
 "t": "t", "t-1": "t-1", "t-2": "t-2", "t-3": "t-3",
 "t2-t+1": "t^2-t+1", "t2+2t+6": "t^2+2*t+6", "t2+t+1": "t^2+t+1", "t2+t+2": "t^2+t+2",
 "t3+2t2+2t-2": "t^3+2*t^2+2*t-2", "t4-t3-t2+t+1": "t^4-t^3-t^2+t+1"}
which = sys.argv[1:] or list(factors)
for name in which:
    g = factors[name]
    lin = g in ("t","t-1","t-2","t-3")
    if lin:
        val = {"t":"0","t-1":"1","t-2":"2","t-3":"3"}[g]
        ring = f'ring r = 0, (t,x1,x2,x3,x4,x5,x6), dp;'
        setup = f'ideal I = fanoideal(); I = I + ideal(t-({val}));'
    else:
        ring = f'ring r = (0,t), (x1,x2,x3,x4,x5,x6), dp; minpoly = {g};'
        setup = 'ideal I = fanoideal();'
    script = f'''< "eig_nf.sing";
{ring}
{setup}
ideal G = std(I);
int dm = dim(G);
printf("FACTOR %s dim %s", "{name}", dm);
if (dm == 0) {{ printf("vdim %s", vdim(G)); }}
list L = primdecGTZ(I);
int i;
for (i=1; i<=size(L); i++) {{
  ideal P = std(L[i][2]);
  printf("  component %s: dim %s vdim %s", i, dim(P), vdim(P));
  P;
}}
quit;
'''
    r = subprocess.run(["Singular","-q","--no-warn"], input=script, capture_output=True, text=True)
    print(r.stdout); print(r.stderr[-500:] if r.stderr else "")
