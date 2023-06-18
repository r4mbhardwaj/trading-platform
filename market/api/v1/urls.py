from django.urls import path

from .views import StockList, StockDetail, PriceList, PriceDetail, get_prices


urlpatterns = [
    path('stocks/', StockList.as_view()),
    path('stocks/<int:pk>/', StockDetail.as_view()),
    path('stocks/<int:pk>/prices/', PriceList.as_view()),
    path('stocks/<int:pk>/prices/<int:price_pk>/', PriceDetail.as_view()),
    path('get_prices/', get_prices), 
]
