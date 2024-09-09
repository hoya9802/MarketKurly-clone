from django.db import models
from users.models import User
from product.models import Products

# models.py

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"User: {self.user.user_id} - Product: {self.product.product_id} (Quantity: {self.quantity})"

    @property
    def total_price(self):
        return self.quantity * self.product.price


