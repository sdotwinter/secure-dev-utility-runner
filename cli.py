import argparse
from pathlib import Path
from transforms import format_json,b64_encode,b64_decode,normalize
from config import load_config, save_config
from policy import check_policy
from audit import log_run, list_runs

def run(argv=None):
    p=argparse.ArgumentParser(prog='secure-dev-utility-runner', description='Local secure utility runner.')
    sub=p.add_subparsers(dest='cmd', required=True)

    j=sub.add_parser('format-json'); j.add_argument('--text', required=True); j.add_argument('path', nargs='?', default='.')
    e=sub.add_parser('b64-encode'); e.add_argument('--text', required=True); e.add_argument('path', nargs='?', default='.')
    d=sub.add_parser('b64-decode'); d.add_argument('--text', required=True); d.add_argument('path', nargs='?', default='.')
    n=sub.add_parser('normalize'); n.add_argument('--text', required=True); n.add_argument('path', nargs='?', default='.')
    a=sub.add_parser('audit'); a.add_argument('path', nargs='?', default='.')
    c=sub.add_parser('config'); c.add_argument('--show', action='store_true'); c.add_argument('path', nargs='?', default='.')

    args=p.parse_args(argv)
    root=Path(getattr(args,'path','.')).resolve()
    cfg=load_config(root)

    if args.cmd == 'audit':
        for r in list_runs(root):
            print(f"[{r[0]}] {r[1]} {r[2]} {r[3]} {r[4]}")
        return 0
    if args.cmd == 'config':
        if args.show:
            print(cfg)
        else:
            save_config(root,cfg)
            print('Config saved')
        return 0

    text=args.text
    ok,msg=check_policy(text,'',cfg)
    if not ok:
        log_run(root,args.cmd,'blocked',msg)
        print(f'Blocked: {msg}')
        return 2

    if args.cmd=='format-json': out=format_json(text)
    elif args.cmd=='b64-encode': out=b64_encode(text)
    elif args.cmd=='b64-decode': out=b64_decode(text)
    elif args.cmd=='normalize': out=normalize(text)
    else: out=''

    log_run(root,args.cmd,'ok','')
    print(out)
    return 0
