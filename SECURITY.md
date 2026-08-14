# Security policy

## Supported scope

This repository contains educational notebook snapshots. Security reports should focus on accidentally committed credentials, personal or restricted data, unsafe default external calls, or dependency risks in the documented reproduction path.

## Credential handling

- Store `GEMINI_API_KEY_INSURANCE_REVIEW` in Kaggle Secrets or a local environment variable.
- Never paste a live credential into a notebook cell, output, issue, or commit.
- The CI workflow does not call external APIs or execute notebook cells.

If a secret is exposed, revoke it with the provider first and then remove it from Git history. Do not open a public issue containing the secret.

## Reporting

Use GitHub’s private vulnerability-reporting feature when it is enabled. Otherwise contact the repository owner privately through the profile’s published contact channel.
