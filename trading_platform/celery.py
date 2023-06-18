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
    'calculate-average-price-every-minute': {
        'task': 'market.tasks.calculate_average_price_minutes',
        'schedule': 60.0,  # Run every minute
    },
    'calculate-average-price-every-hour': {
        'task': 'market.tasks.calculate_average_price_hours',
        'schedule': crontab(minute=0),  # Run every hour at minute 0
    },
    'calculate-average-price-every-day': {
        'task': 'market.tasks.calculate_average_price_days',
        'schedule': crontab(minute=0, hour=0),  # Run every day at 00:00
    },
    'calculate-average-price-every-week': {
        'task': 'market.tasks.calculate_average_price_weeks',
        'schedule': crontab(minute=0, hour=0, day_of_week=1),  # Run every Monday at 00:00
    },
    'calculate-average-price-every-month': {
        'task': 'market.tasks.calculate_average_price_months',
        'schedule': crontab(minute=0, hour=0, day_of_month=1),  # Run on the 1st of every month at 00:00
    },
    'calculate-average-price-every-year': {
        'task': 'market.tasks.calculate_average_price_years',
        'schedule': crontab(minute=0, hour=0, day_of_month=1, month_of_year=1),  # Run on January 1st at 00:00
    },
}
