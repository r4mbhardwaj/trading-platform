from django.shortcuts import render
from rest_framework import generics
from market.models import Stock, Price

from market.serializers import StockSerializer, PriceSerializer

from datetime import timedelta
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

# import Q
from django.db.models import Q
from rest_framework.views import APIView


@csrf_exempt
def get_prices(request):
    if request.method == 'POST':
        ticker = request.POST.get('ticker', '')
        time_period = int(request.POST.get('time_period', 0))
        unit = request.POST.get('unit', 'second')

        end_time = timezone.now()
        if unit == 'second':
            start_time = end_time - timedelta(seconds=time_period)
        elif unit == 'minute':
            start_time = end_time - timedelta(minutes=time_period)
        elif unit == 'hour':
            start_time = end_time - timedelta(hours=time_period)
        elif unit == 'day':
            start_time = end_time - timedelta(days=time_period)
        elif unit == 'week':
            start_time = end_time - timedelta(weeks=time_period)
        elif unit == 'month':
            # Approximate 30 days for a month
            start_time = end_time - timedelta(days=time_period*30)
        elif unit == 'year':
            # Approximate 365 days for a year
            start_time = end_time - timedelta(days=time_period*365)
        else:
            return JsonResponse({'error': 'Invalid unit'}, status=400)

        try:
            stock = Stock.objects.get(ticker=ticker)
        except Stock.DoesNotExist:
            return JsonResponse({'error': 'Stock not found'}, status=404)

        prices = Price.objects.filter(stock=stock, unit=unit, date__range=(
            start_time, end_time)).values('date', 'price')
        data = list(prices)
        return JsonResponse(data, safe=False)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


class AutoCompleteAPI(APIView):
    def get(self, request, format=None):
        query = self.request.GET.get('query', '')
        if query:
            stocks = Stock.objects.filter(
                Q(ticker__icontains=query) | Q(name__icontains=query))
        else:
            stocks = Stock.objects.all()
        data = list(stocks.values('ticker', 'name'))
        return JsonResponse(data, safe=False)


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
