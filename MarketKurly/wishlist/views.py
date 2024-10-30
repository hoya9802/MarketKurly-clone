from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Wishlist
from product.models import Products

from django.contrib.auth.decorators import login_required

@login_required
def wishlist_list(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist/wishlist.html', {
        'wishlist_items': wishlist_items
    })

def add_to_wishlist(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )
    return redirect('wishlist:wishlist_list')

def remove_from_wishlist(request, item_id):
    item = get_object_or_404(Wishlist, id=item_id)
    item.delete()
    return redirect('wishlist:wishlist_list') 
