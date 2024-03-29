import os
from datetime import datetime

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("config")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'create_banned_word': {
#         'task': 'apps.blog.tasks.create_banned_word',
#         'schedule': 60.0 * 5.0,
#         'kwargs': {'date': datetime.strftime('%Y-%m-%d')},
#     }
# }

# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')
