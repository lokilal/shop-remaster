from django.db import models
from pytils.translit import slugify


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название категории')
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['title']


class Item(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название товара')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    image_one = models.CharField(max_length=500, verbose_name='Первое фото')
    image_two = models.CharField(max_length=500, verbose_name='Второе фото')
    image_three = models.CharField(max_length=500, verbose_name='Третье фото')
    descriptions = models.TextField(null=False, verbose_name='Описание товара')
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Item, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        ordering = ['title']
