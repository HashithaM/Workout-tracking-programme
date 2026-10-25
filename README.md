# Pixela Workout Tracker

A command-line exercise that records cycling distance on a Pixela graph using private runtime configuration.

## Workflow

- Prompt for kilometres cycled today
- Format the current date for the Pixela API
- Submit an authenticated pixel to the configured graph

## Requirements

```bash
pip install requests
```

## Secure configuration

Set these environment variables before running the script:

- `PIXELA_USERNAME`
- `PIXELA_TOKEN`
- `PIXELA_GRAPH_ID`

`.env.example` contains dummy values and `.env` is ignored by Git. Never commit an account token.

> [!IMPORTANT]
> Revoke any Pixela token that appeared in an earlier public revision. Replacing the current source does not invalidate an exposed token or erase Git history.

## Run

After securely configuring the variables:

```bash
python main.py
```
