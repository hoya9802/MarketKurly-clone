from django.contrib import admin
from .models import Category, Products

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent_category')

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'owner')