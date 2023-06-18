from django.contrib import admin
from .models import Stock, Price

admin.site.site_header = "Trading Platform Admin"
admin.site.site_title = "Trading Platform Admin Portal"

class StockAdmin(admin.ModelAdmin):
    list_display = ("ticker", "name")
    search_fields = ("ticker", "name")

admin.site.register(Stock, StockAdmin)

class PriceAdmin(admin.ModelAdmin):
    list_display = ("stock", "price", "unit", "date")
    search_fields = ("stock", "price", "unit", "date")
    list_filter = ("stock", "unit")

admin.site.register(Price, PriceAdmin)