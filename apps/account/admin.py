from django.contrib import admin

from .models import CustomeUser


@admin.register(CustomeUser)
class CustomUserManagerAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'username',
        'first_name',
        'last_name',
        'address',
        'phone'
    )
    search_fields = (
        'email',
        'username',
        'first_name',
        'last_name',
        'address',
        'phone'
    )
    ordering = (
        'email',
    )
