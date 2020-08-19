web: gunicorn mysite.wsgi --log-file -
celeryd: celery -A mysite worker -l info -P gevent