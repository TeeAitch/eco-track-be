#!/bin/bash

# create & apply the migrations
python3 manage.py makemigrations authentication core users
python3 manage.py migrate
