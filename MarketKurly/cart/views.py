from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST
from .models import Cart
from wishlist.models import Wishlist  
from product.models import Products

def cart_list(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.total_price for item in cart_items)
    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

def add_to_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        
    wishlist_item = Wishlist.objects.filter(user=request.user, product=product).first()
    if wishlist_item:
        wishlist_item.delete()
        
    return redirect('cart:cart_list')

def update_quantity(request, item_id):
    action = request.POST.get('action')
    item = get_object_or_404(Cart, id=item_id, user=request.user)
    if action == 'increase':
        item.quantity += 1
    elif action == 'decrease' and item.quantity > 1:
        item.quantity -= 1
    item.save()
    return redirect(reverse('cart:cart_list'))

@require_POST
def delete_selected(request):
    selected_ids = request.POST.getlist('selected_items')
    
    if selected_ids:
        # 선택된 항목 삭제
        Cart.objects.filter(id__in=selected_ids, user=request.user).delete()
    
    return redirect(reverse('cart:cart_list'))

