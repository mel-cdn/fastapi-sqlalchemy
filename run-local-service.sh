#!/usr/bin/env bash

set -e -u

export PYTHONPATH=app

echo "> Running local FastAPI service..."
uvicorn app.main:app \
  --env-file .env.local \
  --host 0.0.0.0 \
  --port 9000 \
  --reload
