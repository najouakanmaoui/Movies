from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

__author__ = 'najouakaanmaoui@gmail.com'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movies.settings')
app = Celery(
    "celery_app", broker=settings.CELERY_BROKER_URL, backend=settings.CELERY_BROKER_URL
)
app.autodiscover_tasks()



