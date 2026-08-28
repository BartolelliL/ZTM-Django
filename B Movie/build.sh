#!/usr/bin/env bash
# exit on error
set -o errexit

# Installazione istantanea delle dipendenze da uv.lock
uv sync --frozen

# Esecuzione dei comandi all'interno dell'ambiente di uv
uv run python manage.py collectstatic --no-input
uv run python manage.py migrate