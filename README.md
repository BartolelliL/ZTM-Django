# Working commands UV and DJANGO

```
uv init --bare
uv add django
uv add gunicorn
uv add whitenoise
uv run django-admin startproject config .
uv run python manage.py startapp APP-NAME
```

## To Test it locally:
```
uv run python manage.py runserver
```

## To Deploy it:
```
uv pip freeze > requirements.txt
uv run python manage.py collectstatic
```