from django.shortcuts import render
from .models import Book

def book_list(request):
    template_name = 'library/index.html'
    books = Book.objects.all()
    context = {
        'books': books
    }

    return render(request, template_name, context)