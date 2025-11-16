ALX Travel App (app directory)

This directory contains the Django app code for the ALX Travel App:
- listings app with models, serializers, and seed command
- project configuration (settings, urls, wsgi/asgi)

Quick run
- Migrate: python manage.py makemigrations && python manage.py migrate
- Seed: python manage.py seed --listings 5 --bookings-per-listing 2 --reviews-per-listing 2 --flush


