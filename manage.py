#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# I am commenting this so you can view working
# commands to setup both uv and django

# uv init --bare
# uv add django
# uv run django-admin startproject config .

# To run it:
# uv run python manage.py runserver

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
