import csv, io
from django.shortcuts import render
from freeshelf.models import Book

# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {
        'books': books,
    })

def book_upload(request):
    template = "book_upload.html"
