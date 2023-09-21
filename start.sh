#!/bin/bash

# Make migration
python manage.py migrate

# Run Django-application
python manage.py runserver "0.0.0.0:8000"
