from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'city', 'user', 'photo']
    search_fields = ['id', 'user_username']
