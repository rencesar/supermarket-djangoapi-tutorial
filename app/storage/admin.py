from django.contrib import admin
from django.db.models import Sum

from .models import Section, Products


def calculate_missing_spot_items(obj):
    used_spots = obj.products.aggregate(used_spots=Sum('stock_available'))['used_spots']
    used_spots = used_spots if used_spots is not None else 0
    return obj.max_allowed_items - used_spots


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ["name", "max_allowed_items", calculate_missing_spot_items]


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ["name", "section", "brand", "stock_available"]
