import yaml
from pathlib import Path

def load_policy(path):
    data=yaml.safe_load(Path(path).read_text(encoding='utf-8')) or {}
    data.setdefault('allow', [])
    data.setdefault('timeouts', {})
    return data

def is_allowed(policy, cmd):
    return cmd in set(policy.get('allow', []))

def timeout_for(policy, cmd):
    return int(policy.get('timeouts', {}).get(cmd, 10))
