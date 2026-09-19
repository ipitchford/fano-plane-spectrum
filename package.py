"""Deterministic archive/manifest tool; generated outputs are not proof evidence."""
import argparse
import hashlib
from pathlib import Path
import zipfile
ROOT=Path(__file__).resolve().parent
EXCLUDE={'.git','.venv','__pycache__','dist'}
def files():
    return sorted(p for p in ROOT.rglob('*') if p.is_file() and not any(x in EXCLUDE for x in p.relative_to(ROOT).parts) and p.name!='MANIFEST.sha256' and p.suffix!='.pyc')
def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    parser=argparse.ArgumentParser(); parser.add_argument('mode',choices=['seal','check','zip']); args=parser.parse_args()
    rows=[f'{digest(p)}  {p.relative_to(ROOT).as_posix()}' for p in files()]
    expected='\n'.join(rows)+'\n'; manifest=ROOT/'MANIFEST.sha256'
    if args.mode=='seal':
        manifest.write_text(expected)
    elif manifest.read_text()!=expected:
        raise RuntimeError('Manifest content or coverage mismatch')
    if args.mode=='zip':
        out=ROOT/'dist'; out.mkdir(exist_ok=True)
        target=out/'fano-plane-spectrum-v0.1.0-candidate.zip'
        with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
            for p in files()+[manifest]:
                info=zipfile.ZipInfo('fano-plane-spectrum/'+p.relative_to(ROOT).as_posix(),date_time=(2026,9,19,0,0,0))
                info.compress_type=zipfile.ZIP_DEFLATED; info.external_attr=0o100644<<16
                archive.writestr(info,p.read_bytes())
        print(digest(target),target)
    print('PASS',len(rows),'manifest entries')
if __name__=='__main__':
    main()
