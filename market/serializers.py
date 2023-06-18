from .models import Stock, Price
from rest_framework import serializers

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('name', 'ticker')

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('id', 'stock', 'date', 'price')