# tasks.py
from celery import shared_task
import random
import datetime

from .models import Stock, Price

@shared_task
def generate_price():
    stocks = Stock.objects.all()
    for stock in stocks:

        price_value = random.uniform(random.randint(300, 800), random.randint(800, 1400))  # Generate a random price
        price = Price(stock=stock, date=datetime.datetime.now(), price=price_value)
        price.save()