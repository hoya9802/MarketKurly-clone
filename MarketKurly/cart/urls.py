from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_list, name='cart_list'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update_quantity/<int:item_id>/', views.update_quantity, name='update_quantity'),
    path('delete_selected/', views.delete_selected, name='delete_selected'),
]

