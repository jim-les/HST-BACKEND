#!/usr/bin/env bash
# Build script for the project
# exit on error
set -e errexit

pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
