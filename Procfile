web: gunicorn mysite.wsgi --log-file -
worker: celery -A mysite worker -l info -P gevent