from django.db import models
from django.conf import settings
from product.models import Products
from users.models import User

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)  # Optional: if you need to track when items are added

    @property
    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'{self.product.name} in cart of {self.user.username}'

