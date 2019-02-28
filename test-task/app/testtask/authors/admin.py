from django.contrib import admin
from .models import Author

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Author', {
            'fields': (
                ('first_name', 'last_name'),
                ('birthday', 'sex')
            ),
        }),
    ]
    ordering = ['last_name']