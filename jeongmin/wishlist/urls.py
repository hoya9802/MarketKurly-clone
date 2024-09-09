from django.urls import path
from .views import WishlistView, WishlistAddView, WishlistDeleteView


app_name = 'wishlist'

urlpatterns = [
    path('', WishlistView.as_view(), name='wishlist'),
    path('add/<int:product_id>/', WishlistAddView.as_view(), name='wishlist_add'),
    path('delete/<int:wishlist_id>/', WishlistDeleteView.as_view(), name='wishlist_delete'),
]