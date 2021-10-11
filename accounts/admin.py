from django.contrib import admin
from accounts.models import Cart


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'number',
        'date',
        'status',
    )

    search_fields = ('date',)
    list_filter = ('date',)



