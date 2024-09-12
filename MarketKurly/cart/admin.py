from django.contrib import admin
from .models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'total_price', 'added_at')  
    list_filter = ('user', 'product') 

admin.site.register(Cart, CartAdmin)

