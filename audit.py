import sqlite3
from pathlib import Path
from datetime import datetime

def db_path(root: Path): return root / '.secure_runner_audit.db'

def init_db(root: Path):
    c=sqlite3.connect(db_path(root))
    c.execute('CREATE TABLE IF NOT EXISTS runs(id INTEGER PRIMARY KEY AUTOINCREMENT, ts TEXT, command TEXT, status TEXT, note TEXT)')
    c.commit(); c.close()

def log_run(root: Path, command: str, status: str, note: str=''):
    init_db(root)
    c=sqlite3.connect(db_path(root))
    c.execute('INSERT INTO runs(ts,command,status,note) VALUES (?,?,?,?)',(datetime.utcnow().isoformat()+'Z',command,status,note))
    c.commit(); c.close()

def list_runs(root: Path, limit=20):
    init_db(root)
    c=sqlite3.connect(db_path(root))
    rows=c.execute('SELECT id,ts,command,status,note FROM runs ORDER BY id DESC LIMIT ?', (limit,)).fetchall()
    c.close(); return rows
