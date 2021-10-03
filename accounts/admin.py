from django.contrib import admin
from .models import Order, Cart


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'number',
        'date',
        'status',
    )

    search_fields = ('date',)
    list_filter = ('date',)


admin.site.register(Order, PostAdmin)
