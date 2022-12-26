from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # This will display the fields in the admin interface
    list_display = ('title', 'author', 'publisher', 'publication_date')

admin.site.register(Book, BookAdmin)
