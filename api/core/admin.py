from django.contrib import admin
from .models import Book, Ebook


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'city', 'user', 'photo']
    search_fields = ['id', 'user_username']


@admin.register(Ebook)
class EbookAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'user', 'ebook']
    search_fields = ['id', 'user_username']
