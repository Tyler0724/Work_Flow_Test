# Security Scan Demo

End-to-end demo that runs Safety on intentionally vulnerable dependencies, converts the JSON output to SARIF, and uploads to GitHub Code Scanning.

## What this repo contains
- Workflow: `.github/workflows/security-scan.yml` runs Safety, calls the SARIF converter action, and uploads SARIF with `github/codeql-action/upload-sarif@v3` (requires `security-events: write`).
- Vulnerable sample: `vulnerable-app/` with outdated dependencies and insecure code paths to generate findings.
- Evidence: `screenshots/` placeholder for workflow run, alerts list, and alert detail captures.

## Local smoke test
```bash
python -m pip install safety
cd vulnerable-app
safety scan --file requirements.txt --output json --continue-on-error > ../safety-output.json
cd ..
python ../safety-sarif-action/converter.py --input safety-output.json --output safety.sarif --manifest vulnerable-app/requirements.txt
```
Inspect `safety.sarif` then upload with the workflow or `upload-sarif` action.

