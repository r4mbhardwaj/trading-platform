from django.urls import path, include

# after /api/auth/...
urlpatterns = [
    # API views
    path('v1/', include(('authenty.api.v1.urls', 'v1'), namespace='v1')),
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),

    # UI views
]