import argparse
import json
from policy import load_policy, is_allowed, timeout_for
from runner import execute
from audit import append, history


def run(argv=None):
    p = argparse.ArgumentParser(prog='secure-dev-utility-runner')
    sub = p.add_subparsers(dest='action', required=True)

    run_cmd = sub.add_parser('run')
    run_cmd.add_argument('--policy', required=True)
    run_cmd.add_argument('--command', required=True)

    check_cmd = sub.add_parser('check')
    check_cmd.add_argument('--policy', required=True)
    check_cmd.add_argument('--command', required=True)

    hist_cmd = sub.add_parser('history')
    hist_cmd.add_argument('--limit', type=int, default=20)

    pol_cmd = sub.add_parser('policy')
    pol_cmd.add_argument('--file', required=True)

    args = p.parse_args(argv)

    if args.action == 'policy':
        pol = load_policy(args.file)
        print(json.dumps(pol, indent=2))
        return 0

    if args.action == 'history':
        for ln in history(args.limit):
            print(ln)
        return 0

    pol = load_policy(args.policy)
    cmd = args.command
    allowed = is_allowed(pol, cmd)

    if args.action == 'check':
        rec = {'action': 'check', 'allowed': allowed, 'command': cmd}
        append(rec)
        print({'allowed': allowed, 'command': cmd})
        return 0 if allowed else 1

    if args.action == 'run':
        if not allowed:
            append({'action': 'run', 'allowed': False, 'command': cmd, 'code': None})
            print('Blocked by policy: command not allowlisted')
            return 1

        res = execute(cmd, timeout=timeout_for(pol, cmd))
        append({'action': 'run', 'allowed': True, 'command': cmd, 'code': res['code']})
        print(json.dumps(res, indent=2))
        return int(res['code'])

    return 0
