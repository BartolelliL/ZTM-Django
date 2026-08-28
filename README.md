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

## To Build it:
```
chmod +x ./build.sh 
./build.sh
```