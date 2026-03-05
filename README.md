# Secure Dev Utility Runner

[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ea4aaa?logo=githubsponsors)](https://github.com/sponsors/sdotwinter)

Local-first CLI for safe developer utility transforms with policy guardrails and audit logging.

## Usage
```bash
python3 main.py format-json --text '{"b":2,"a":1}' .
python3 main.py b64-encode --text 'hello' .
python3 main.py b64-decode --text 'aGVsbG8=' .
python3 main.py normalize --text 'hello   world\nfoo' .
python3 main.py audit .
python3 main.py config --show .
```

## Sponsorware
Personal evaluation is free. Commercial/team usage and advanced policy packs require sponsorship.
Suggested tiers: **$7 / $14 / $50**.
