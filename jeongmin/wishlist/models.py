from django.db import models
from users.models import User
from product.models import Products

# Create your models here.
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return f"Product ID: {self.user.user_id}- {self.product.product_id}"