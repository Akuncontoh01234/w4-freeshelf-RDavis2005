import csv, io
from django.shortcuts import render
from freeshelf.models import Book, Category

# Create your views here.
def index(request):
    books = Book.objects.all().order_by('date_added')
    return render(request, 'index.html', {
        'books': books,
    })

def book_upload(request):
    template = "book_upload.html"

def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'books/book_detail.html', {
        'book': book,
    })

def category(request, slug):
    category = Category.objects.get(slug=slug)
    return render(request, 'categories/category_detail.html', { 
        'category': category,
    })