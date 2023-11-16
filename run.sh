#!/bin/bash

python manage.py makemigrations
python manage.py migrate
python manage.py initadmin
python manage.py runserver
