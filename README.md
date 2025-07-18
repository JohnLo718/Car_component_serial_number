# Car Component Serial Number Finder

This repository contains a small Streamlit application for managing cars and their component serial numbers.
You can compare cars, list their components, add or edit entries, and now delete cars or individual components with confirmation.

## Running locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Docker

Build the container and run it on port 8080:

```bash
docker build -t serialfinder .
docker run -p 8080:8080 serialfinder
```

The app is designed to work well on Google Cloud Run where the container listens on port `8080`.

## GitHub auto-sync

Any changes made to `data/serial_numbers.json` through the Streamlit UI are automatically pushed back to the GitHub repository. Set the `GITHUB_TOKEN` environment variable with a Personal Access Token that has permission to update the repository (typically the `repo` scope).
