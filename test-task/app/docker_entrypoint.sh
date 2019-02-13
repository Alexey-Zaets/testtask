#!/bin/bash

# Collect static files
echo """
*
*
Collect static files
======================================================================
"""
python testtask/manage.py collectstatic --noinput


# Apply database migrations
echo """
*
*
Apply database migrations
======================================================================
"""
python testtask/manage.py makemigrations && python testtask/manage.py migrate


# Run Main service
echo """
*
*
Start Gunicorn
======================================================================
"""
gunicorn --config ./gunicorn_config.py testtask.wsgi:application

