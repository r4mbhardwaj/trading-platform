from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from authenty.models import WishlistStock
from authenty.serializers import WishlistStockSerializer

# csrf_exempt
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# wishlist of user only where user is the owner of the wishlist
class WishlistStockListView(generics.ListAPIView):
    serializer_class = WishlistStockSerializer

    def get_queryset(self):
        user = self.request.user
        return WishlistStock.objects.filter(user=user)

class WishlistStockCreateView(generics.CreateAPIView):
    serializer_class = WishlistStockSerializer

    def perform_create(self, serializer):
        # see if already exist
        user = self.request.user
        stock_pk = self.request.data.get('stock')
        qs = WishlistStock.objects.filter(user=user, stock__pk=stock_pk)
        if qs.exists():
            raise serializers.ValidationError("Already in wishlist")
        serializer.save(user=user)



@method_decorator(csrf_exempt, name='dispatch')
class WishlistStockDeleteView(APIView):
    def post(self, request, *args, **kwargs):
        user = self.request.user
        stock_pk = request.data.get('stock')
        qs = WishlistStock.objects.filter(user=user, stock__pk=stock_pk)
        if qs.exists():
            qs.first().delete()
            return Response({"message": "Successfully removed from wishlist"}, status=200)
        return Response({"message": "Error removing from wishlist"}, status=400)