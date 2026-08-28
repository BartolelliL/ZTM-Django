#!/usr/bin/env bash
# exit on error
set -o errexit

pip install uv

# sync dependences
uv sync --frozen

# static files & db migration
uv run python manage.py collectstatic --no-input
uv run python manage.py migrate