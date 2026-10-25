import os
from datetime import datetime

import requests


PIXELA_ENDPOINT = "https://pixe.la/v1/users"


def required_env(name):
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def main():
    username = required_env("PIXELA_USERNAME")
    token = required_env("PIXELA_TOKEN")
    graph_id = required_env("PIXELA_GRAPH_ID")

    today = datetime.now()
    pixel_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs/{graph_id}"
    pixel_data = {
        "date": today.strftime("%Y%m%d"),
        "quantity": input("How many kilometers did you cycle today? "),
    }
    headers = {"X-USER-TOKEN": token}

    response = requests.post(
        url=pixel_endpoint,
        json=pixel_data,
        headers=headers,
        timeout=30,
    )
    response.raise_for_status()
    print(response.text)


if __name__ == "__main__":
    main()
