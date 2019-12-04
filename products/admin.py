from django.contrib import admin
from .models import Size, Color, Product


@admin.register(Size)
class SizeModelAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id', 'title', 'description']
    list_display_links = ['title']
    list_filter = ['title']
    search_fields = ['title']


@admin.register(Color)
class ColorModelAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id', 'title', 'color_code']
    list_display_links = ['title']
    list_filter = ['title']
    search_fields = ['title']


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['pid', 'title', 'slug', 'in_stock', 'stocks']
    list_display_links = ['pid', 'title', 'slug']
    list_filter = ['title', 'pid', 'slug']
    search_fields = ['title', 'pid', 'slug']
