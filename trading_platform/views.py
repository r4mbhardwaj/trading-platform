from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class WishlistView(TemplateView):
    template_name = 'wishlist.html'