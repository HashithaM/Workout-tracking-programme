# Pixela Workout Tracker

A command-line exercise that records cycling distance on a Pixela graph. The source also includes examples for creating a user and graph and for updating or deleting a daily pixel.

## Workflow

- Prompt for kilometres cycled today
- Format the current date for the Pixela API
- Submit an authenticated pixel to the configured graph
- Provide commented examples for graph creation, updates, and deletion

## Requirements

```bash
pip install requests
```

## Security warning

> [!CAUTION]
> The current source contains a user-scoped Pixela token. Treat it as exposed: rotate it, remove it from public source/history, and load the replacement from an environment variable or secret manager.

The username, graph ID, and token should all be external configuration. Never commit account tokens.

## Run

After rotating and safely configuring the token:

```bash
python main.py
```
