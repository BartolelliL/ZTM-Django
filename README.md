# Working commands UV and DJANGO

## Init:

```
uv init --bare
uv add django 
# uv add gunicorn
# uv add whitenoise
uv run django-admin startproject config .
uv run python manage.py startapp APP-NAME
uv run python manage.py createsuperuser
```

## To test the project locally:

```
uv run python manage.py runserver
```

## To update the db:

```
uv run python manage.py makemigrations
uv run python manage.py migrate
```

## To Build it:

```
chmod +x ./build.sh 
./build.sh
```