from django.shortcuts import render
from rest_framework import generics
from market.models import Stock, Price

from market.serializers import StockSerializer, PriceSerializer

class StockList(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    paginate_by = 10

class StockDetail(generics.RetrieveAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class PriceList(generics.ListAPIView):
    # get price of a stock
    serializer_class = PriceSerializer
    paginate_by = 10

    def get_queryset(self):
        stock_id = self.kwargs['pk']
        return Price.objects.filter(stock_id=stock_id)
    
class PriceDetail(generics.RetrieveAPIView):
    # get price of a stock
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
