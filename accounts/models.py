from django.db import models
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


class Order(models.Model):
    STATUS_ORDER = [
        ('Принято', 'Принято'),
        ('Изготавливается', 'Изготавливается'),
        ('Доставляется', 'Доставляется'),
        ('Доставлено', 'Доставлено')
    ]
    user = models.CharField(max_length=100, default='', verbose_name="Пользователь")
    user_name = models.CharField(max_length=100, default='', verbose_name="Имя")
    product = models.TextField(max_length=2000, verbose_name="Продукты")
    number = models.CharField(max_length=100, default='', verbose_name="Телефон")
    status = models.CharField(max_length=15, choices=STATUS_ORDER, default='1')
    date = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Дата")

    class Meta:
        ordering = ['-date']