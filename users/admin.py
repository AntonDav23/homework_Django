from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "username", "phone", "country", "is_staff")
    ordering = ("email",)
    search_fields = ("email", "username", "phone")
