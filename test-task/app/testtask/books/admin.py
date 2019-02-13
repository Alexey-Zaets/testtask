from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Книга', {
            'fields':(('title', 'isbn'),('genre', 'pub_date'), 'authors'),
        }),
    ]
    ordering = ['pub_date', 'title']
    filter_horizontal = ['authors']