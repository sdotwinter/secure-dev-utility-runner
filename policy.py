from pathlib import Path

def check_policy(text: str, target_path: str, cfg: dict):
    for pat in cfg.get('blockedPatterns', []):
        if pat.lower() in text.lower():
            return False, f'Blocked pattern detected: {pat}'
    tp = str(target_path or '')
    for p in cfg.get('blockedPaths', []):
        if tp.startswith(p):
            return False, f'Blocked path detected: {p}'
    return True, ''
