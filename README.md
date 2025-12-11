# Security Scan Demo

This demo repository layout shows how to run the Safety scanner, convert its JSON output to SARIF with the custom action, and upload findings to GitHub Advanced Security Code Scanning.

## What this demo includes
- Workflow at `demo/.github/workflows/security-scan.yml` that runs Safety, calls the SARIF converter action, and uploads the SARIF with `github/codeql-action/upload-sarif@v3` (requires `security-events: write`).
- A vulnerable sample app in `demo/vulnerable-app/` with intentionally outdated dependencies (5+ distinct issues across severities).
- `demo/screenshots/` placeholder for evidence of successful runs and Code Scanning alerts.

## How to use
1) Create a new public repo and copy the contents of `demo/` into its root.
2) Update the workflow to point to your published action tag: replace `your-username/safety-sarif-action@v1` with the released action.
3) Commit and push. Ensure `Actions` are enabled and rerun if needed.
4) After two successful runs, capture screenshots:
   - Workflow run succeeding.
   - Code Scanning alerts list.
   - Alert detail showing file/line mapping.
5) Place screenshots in `demo/screenshots/` (or the equivalent folder in the demo repo) and reference them from the README.

## Expected results
- Safety reports vulnerable dependencies from `vulnerable-app/requirements.txt`.
- The converter emits a SARIF file (`safety.sarif`) that uploads successfully.
- Code Scanning shows alerts with severity mapping that matches Safety’s reported severities.
