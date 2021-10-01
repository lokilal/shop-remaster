from django.contrib import admin
from .models import Category, Item


class MarketAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'price',
        'category',
    )
    search_fields = ('title', 'price', )
    list_filter = ('price',)
    empty_value_display = '-пусто-'


admin.site.register(Category)
admin.site.register(Item, MarketAdmin)
