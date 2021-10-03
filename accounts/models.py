from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from market.models import Item


class Cart(models.Model):
    user = models.CharField(max_length=150, null=True)


class CartItem(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(blank=True)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)

    def __str__(self):
        return self.cart.user + " - " + self.product.title
