from django.urls import path, include
from .views import WishlistStockListView, WishlistStockCreateView, WishlistStockDeleteView

# after /api/auth/...
urlpatterns = [
    path('wishlist/', WishlistStockListView.as_view(), name='wishlist-list'),
    path('wishlist/create/', WishlistStockCreateView.as_view(), name='wishlist-create'),
    path('wishlist/delete/', WishlistStockDeleteView.as_view(), name='wishlist-delete'),
]