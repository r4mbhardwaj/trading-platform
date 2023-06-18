from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.registration.views import SocialAccountListView
from .views import HomeView, WishlistView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include(('authenty.urls', 'authenty'), namespace='authenty')),
    path('accounts/', include('allauth.urls')),
    # add market with market as namespace, so in templates we can use market:stock_list
    path('market/', include(('market.urls', 'market'), namespace='market')),
    path("", HomeView.as_view(), name="home"),
    path("wishlist/", WishlistView.as_view(), name="wishlist"),
]