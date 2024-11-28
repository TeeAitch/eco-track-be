#!/bin/bash

# clear the db and create a new one with the migrations and create superuser
rm -rf apps/**/__pycache__/
rm -rf apps/**/migrations/*

rm db.sqlite3

python manage.py makemigrations

python manage.py migrate admin zero
python manage.py migrate auth zero
python manage.py migrate contenttypes zero
python manage.py migrate sessions zero

# comment out only when db not deleted: python manage.py migrate

python manage.py makemigrations

python manage.py makemigrations core
python manage.py makemigrations users

python manage.py migrate

python3 manage.py createsuperuser


