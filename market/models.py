from django.db import models
from django.urls import reverse
from datetime import datetime, timedelta

class Stock(models.Model):
    name = models.CharField(max_length=100) # Name of the stock
    ticker = models.CharField(max_length=10, primary_key=True) # Ticker is the stock symbol
    starting_price = models.FloatField(default=0) # Starting price of the stock
    volatility = models.FloatField(default=0.15) # Volatility of the stock
    def __str__(self):
        return f"${self.ticker}"
    
    def get_absolute_url(self):
        return reverse('market:stock_detail', kwargs={'slug': self.ticker})
    
    def get_yesterday_price(self):
        yesterday = datetime.now() - timedelta(days=1)
        prices = Price.objects.filter(stock=self, unit='day', date__date=yesterday.date()).order_by('-date')
        if prices.exists():
            return prices.first().price
        else:
            return None

    def get_current_price(self):
        return self.price_set.order_by('-date')[0].price


TIME_UNITS = (
    ('second', 'second'),
    ('minute', 'minute'),
    ('hour', 'hour'),
    ('day', 'day'),
    ('week', 'week'),
    ('month', 'month'),
    ('year', 'year'),
)

class Price(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE) # A stock can have many prices
    date = models.DateTimeField(auto_now_add=True) # Date of the price
    price = models.FloatField()
    unit = models.CharField(max_length=10, default='second', choices=TIME_UNITS)
    def __str__(self):
        return str(self.stock) + " " + str(self.date) + " " + str(self.price)