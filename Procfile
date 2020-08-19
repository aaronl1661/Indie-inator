web: gunicorn mysite.wsgi --log-file -
worker: celery -A products.tasks worker -l info -P gevent