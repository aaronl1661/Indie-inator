from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
#app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.update(
    broker_url = 'redis://h:p5724480c90c96c86c0863933d4b8fee1adf95eedcf45ae93845742edfeb196f3@ec2-54-242-155-141.compute-1.amazonaws.com:23559',
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    result_backend='django-db',
)
# Load task modules from all registered Django app configs.
app.autodiscover_tasks('packages')


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))