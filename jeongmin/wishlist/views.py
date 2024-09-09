from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Wishlist
from product.models import Products

class WishlistView(View):
    def get(self, request):
        wishlist = Wishlist.objects.filter(user=request.user)
        return render(request, 'wishlist/wishlist.html', {'wishlist': wishlist})

class WishlistAddView(View):
    def post(self, request, product_id):
        product = get_object_or_404(Products, id=product_id)
        Wishlist.objects.get_or_create(user=request.user, product=product)
        return redirect('wishlist:wishlist')

class WishlistDeleteView(View):
    def post(self, request, wishlist_id):
        wishlist = get_object_or_404(Wishlist, id=wishlist_id, user=request.user)
        wishlist.delete()
        return redirect('wishlist:wishlist')