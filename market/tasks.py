# tasks.py
from datetime import datetime, timedelta
from .models import Price, TIME_UNITS
from celery import shared_task
import random

from .models import Stock, Price
from django.db import models


@shared_task
def generate_price():
    stocks = Stock.objects.all()
    for stock in stocks:
        starting_price = stock.starting_price
        try:
            current_price = stock.get_current_price()
        except:
            current_price = None
        if not current_price:
            current_price = starting_price
        new_price = current_price * random.uniform(0.97, 1.03)
        # add or subtract a random number between -3 and 3
        new_price = new_price + random.randint(-3, 3)

        # make it positive if it's negative
        if new_price < 0:
            new_price = new_price * -1

        # Save the updated price
        price = Price(stock=stock, date=datetime.now(), price=new_price)
        price.save()



@shared_task
def calculate_average_price_minutes():
    stocks = Stock.objects.all()
    for stock in stocks:
        end_time = datetime.now()
        start_time = end_time - timedelta(minutes=1)
        prices = Price.objects.filter(
            stock=stock, unit='second', date__range=(start_time, end_time))
        if prices.exists():
            average_price = prices.aggregate(models.Avg('price'))['price__avg']
            Price.objects.create(
                stock=stock, price=average_price, unit='minute')


@shared_task
def calculate_average_price_hours():
    stocks = Stock.objects.all()
    for stock in stocks:
        end_time = datetime.now()
        start_time = end_time - timedelta(hours=1)
        prices = Price.objects.filter(
            stock=stock, unit='minute', date__range=(start_time, end_time))
        if prices.exists():
            average_price = prices.aggregate(models.Avg('price'))['price__avg']
            Price.objects.create(stock=stock, price=average_price, unit='hour')


@shared_task
def calculate_average_price_days():
    stocks = Stock.objects.all()
    for stock in stocks:
        end_time = datetime.now()
        start_time = end_time - timedelta(days=1)
        prices = Price.objects.filter(
            stock=stock, unit='hour', date__range=(start_time, end_time))
        if prices.exists():
            average_price = prices.aggregate(models.Avg('price'))['price__avg']
            Price.objects.create(stock=stock, price=average_price, unit='day')


@shared_task
def calculate_average_price_weeks():
    stocks = Stock.objects.all()
    for stock in stocks:
        end_time = datetime.now()
        start_time = end_time - timedelta(weeks=1)
        prices = Price.objects.filter(
            stock=stock, unit='day', date__range=(start_time, end_time))
        if prices.exists():
            average_price = prices.aggregate(models.Avg('price'))['price__avg']
            Price.objects.create(stock=stock, price=average_price, unit='week')


@shared_task
def calculate_average_price_months():
    stocks = Stock.objects.all()
    for stock in stocks:
        end_time = datetime.now()
        start_time = end_time - timedelta(days=30)
        prices = Price.objects.filter(
            stock=stock, unit='week', date__range=(start_time, end_time))
        if prices.exists():
            average_price = prices.aggregate(models.Avg('price'))['price__avg']
            Price.objects.create(
                stock=stock, price=average_price, unit='month')


@shared_task
def calculate_average_price_years():
    stocks = Stock.objects.all()
    for stock in stocks:
        end_time = datetime.now()
        start_time = end_time - timedelta(days=365)
        prices = Price.objects.filter(
            stock=stock, unit='month', date__range=(start_time, end_time))
        if prices.exists():
            average_price = prices.aggregate(models.Avg('price'))['price__avg']
            Price.objects.create(stock=stock, price=average_price, unit='year')
