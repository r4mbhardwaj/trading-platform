# authenty/serializers.py

from .models import WishlistStock
from rest_framework import serializers


class WishlistStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistStock
        # make user request.user automatically and not editable
        exclude = ('user', 'id',)