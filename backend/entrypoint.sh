#!/bin/bash

echo "Installing requirements"
pip install -r /code/requirements.txt

echo "Applying Migrations"
python3 manage.py makemigrations

python3 manage.py migrate --noinput

echo "Starting Server FutbolApp Backend"
python3 manage.py runserver 0.0.0.0:8000