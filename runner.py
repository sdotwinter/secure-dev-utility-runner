import subprocess

def execute(cmd, timeout=10):
    r=subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
    return {'code': r.returncode, 'stdout': r.stdout, 'stderr': r.stderr}
