from django.urls import path, include
from .views import Search, StockListView, StockDetailView

urlpatterns = [
    # API versions
    path('api/v1/', include('market.api.v1.urls')),

    # UI urls
    path('', Search.as_view(), name='stock_search'),
    path('stocks/', StockListView.as_view(), name='stock_list'),
    path('stocks/<slug:slug>/', StockDetailView.as_view(), name='stock_detail'),
]
