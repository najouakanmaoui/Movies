#!/bin/sh

echo "Waiting for PostgreSQL to be ready..."
until pg_isready -h postgres -p 5432 -q; do
    echo "PostgreSQL is not ready yet. Retrying in 1 second..."
    sleep 1
done
echo "PostgreSQL is ready."

service redis-server start
python manage.py makemigrations
python manage.py migrate
python movies/seed.py
python manage.py runserver 0.0.0.0:8081
