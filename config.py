from pathlib import Path
import json

def cfg_path(root: Path) -> Path:
    return root / 'secure_runner_config.json'

def load_config(root: Path) -> dict:
    p=cfg_path(root)
    if not p.exists():
        return {'blockedPatterns':['PRIVATE KEY','BEGIN RSA'], 'blockedPaths':['/etc/','/root/']}
    return json.loads(p.read_text(encoding='utf-8'))

def save_config(root: Path, cfg: dict) -> None:
    cfg_path(root).write_text(json.dumps(cfg, indent=2) + '\n', encoding='utf-8')
