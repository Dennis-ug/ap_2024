#!/bin/sh

set -e

echo "Collecting static files"
echo "=================================================================="
python  manage.py collectstatic --no-input

python manage.py makemigrations --no-input
echo "Making migration\n"
echo "Making database migrations"
python manage.py migrate --no-input

echo "Starting server"
echo "================================================================="
gunicorn gunicorn --bind 0.0.0.0:8000 ap_website.wsgi:application





exec "$@"
