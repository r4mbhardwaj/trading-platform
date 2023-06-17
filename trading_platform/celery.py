# celery.py

import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trading_platform.settings')

app = Celery('trading_platform')
app.config_from_object(settings, namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'generate-price-every-second': {
        'task': 'market.tasks.generate_price',
        'schedule': 1.0,  # Run every second
    },
}
