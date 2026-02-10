---
name: verify-gateways
description: Verifies the status of all configured LiteLLM gateways by pinging them with a test prompt.
---

# Verify Gateways

This skill runs a Python script to verify that all configured tiers in `config.yaml` are reachable and responding.

## Usage

1. Ensure the docker containers are running:
   ```bash
   docker-compose up -d
   ```
2. Run the verification script:
   ```bash
   python3 .agent/skills/verify-gateways/verify.py
   ```

## Expected Output

The script will output a table of status results for each model alias.
 - **PASS**: Model responded with 200 OK.
 - **FAIL**: Model returned an error (check logs).
