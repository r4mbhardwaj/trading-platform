from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.registration.views import SocialAccountListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authenty.urls')),
]