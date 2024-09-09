from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Cart
from product.models import Products

# Cart Views
class CartView(View):
    def get(self, request):
        cart = Cart.objects.filter(user=request.user)
        total_price = sum(cart.total_price() for cart in cart)
        return render(request, 'cart/cart.html', {'cart': cart, 'total_price': total_price})

class CartAddView(View):
    def post(self, request, product_id):
        product = get_object_or_404(Products, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart.quantity += 1
        cart.save()
        return redirect('cart:cart')

class CartUpdateView(View):
    def post(self, request, cart_id):
        cart = get_object_or_404(Cart, id=cart_id, user=request.user)
        quantity = request.POST.get('quantity')
        if quantity:
            cart.quantity = int(quantity)
            cart.save()
        return redirect('cart:cart')

class CartDeleteView(View):
    def post(self, request, cart_id):
        cart = get_object_or_404(Cart, id=cart_id, user=request.user)
        cart.delete()
        return redirect('cart:cart')

