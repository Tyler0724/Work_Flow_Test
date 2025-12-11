# Security Scan Demo

This demo repository layout shows how to run the Safety scanner, convert its JSON output to SARIF with the custom action, and upload findings to GitHub Advanced Security Code Scanning.

## What this demo includes
- Workflow at `.../.github/workflows/security-scan.yml` that runs Safety, calls the SARIF converter action, and uploads the SARIF with `github/codeql-action/upload-sarif@v3` (requires `security-events: write`).
- A vulnerable sample app in `.../vulnerable-app/` with intentionally outdated dependencies (5+ distinct issues across severities).
- `.../screenshots/` placeholder for evidence of successful runs and Code Scanning alerts.

## Expected results
- Safety reports vulnerable dependencies from `vulnerable-app/requirements.txt`.
- The converter emits a SARIF file (`safety.sarif`) that uploads successfully.
- Code Scanning shows alerts with severity mapping that matches Safety’s reported severities.
