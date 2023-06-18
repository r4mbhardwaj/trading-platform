from django.db import models
from django.conf import settings
from market.models import Stock

class WishlistStock(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wishlist')
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='wishlisted_by')

    def __str__(self):
        return self.stock.name
    
    class Meta:
        unique_together = ('user', 'stock')