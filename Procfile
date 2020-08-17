web: gunicorn mysite.wsgi --log-file -
worker: python manage.py celery worker --beat --loglevel=info