# Car Component Serial Number Finder

This repository contains a small Streamlit application for managing cars and their component serial numbers.

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
