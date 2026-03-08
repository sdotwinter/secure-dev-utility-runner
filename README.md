# Secure Dev Utility Runner

[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ea4aaa?logo=githubsponsors)](https://github.com/sponsors/sdotwinter)

Run approved developer utilities with guardrails and audit logs.

## Usage
```bash
python3 main.py policy --file samples/policy.yaml
python3 main.py check --policy samples/policy.yaml --command "echo hello"
python3 main.py run --policy samples/policy.yaml --command "echo hello"
python3 main.py history --limit 10
```

## Sponsorware
Personal use is free. Team templates and policy packs require sponsorship.
Suggested tiers: **$7 / $14 / $50**.
