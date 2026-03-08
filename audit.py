from pathlib import Path
from datetime import datetime
import json

AUDIT=Path.home()/'.secure-dev-runner'/'audit.log'

def append(entry):
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    rec={'ts':datetime.utcnow().isoformat()+'Z', **entry}
    with AUDIT.open('a', encoding='utf-8') as f:
        f.write(json.dumps(rec)+'\n')

def history(limit=20):
    if not AUDIT.exists():
        return []
    lines=AUDIT.read_text(encoding='utf-8').splitlines()
    return lines[-limit:]
