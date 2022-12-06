#!/bin/sh
gunicorn --chdir app main:app -w 2 --threads 2 -b 0.0.0.0:8000 --reload
gunicorn main:app -c gunicorn.config.py