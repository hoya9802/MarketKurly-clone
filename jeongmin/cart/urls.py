from django.urls import path
from .views import CartView, CartAddView, CartUpdateView, CartDeleteView
app_name = 'cart'

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add/<int:product_id>/', CartAddView.as_view(), name='cart_add'),
    path('update/<int:cart_id>/', CartUpdateView.as_view(), name='cart_update'),
    path('delete/<int:cart_id>/', CartDeleteView.as_view(), name='cart_delete'),
]

