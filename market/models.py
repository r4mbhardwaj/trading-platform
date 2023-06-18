from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length=100) # Name of the stock
    ticker = models.CharField(max_length=10, primary_key=True) # Ticker is the stock symbol
    def __str__(self):
        return f"${self.ticker}"
    
class Price(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE) # A stock can have many prices
    date = models.DateTimeField(auto_now_add=True) # Date of the price
    price = models.FloatField()
    def __str__(self):
        return str(self.stock) + " " + str(self.date) + " " + str(self.price)