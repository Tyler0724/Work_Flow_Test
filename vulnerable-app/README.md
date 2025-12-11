# Vulnerable App

Purpose-built sample to generate Safety findings for the SARIF upload workflow.

## Intentional vulnerabilities (dependencies)
- Flask 0.12.2 — known Remote Code Execution (High).
- requests 2.19.0 — credential exposure on redirect (High).
- PyYAML 5.3 — unsafe load RCE vector (High).
- Pillow 5.1.0 — multiple memory corruption issues (Medium/High).
- cryptography 3.3.1 — padding oracle / memory issues (Medium).

## Intentional vulnerabilities (code)
- Unsafe `yaml.load` without SafeLoader.
- Hardcoded API key (`FAKE_API_KEY`).
- SQL injection via string interpolation.
- Arbitrary code execution via `eval`.

## Running locally
```
python -m pip install safety
safety scan --file requirements.txt --output json --continue-on-error
```

This output is what the demo workflow converts to SARIF and uploads to GitHub Code Scanning.
