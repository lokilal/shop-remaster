from django.db import models


class ItemInCart(models.Model):
    price = models.IntegerField()
    amount = models.IntegerField()
    title = models.CharField(max_length=75)


class Cart(models.Model):
    amount = models.TextField(max_length=200, verbose_name="Количество")
    user = models.CharField(max_length=100, default='', verbose_name="Пользователь")
    product = models.ForeignKey(ItemInCart, on_delete=models.CASCADE)
    #product = models.TextField(max_length=2000, verbose_name="Продукты")


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
