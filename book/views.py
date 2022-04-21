from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book, Author
from .forms import BookForm
import os

# Create your views here.


def index(request):
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, "book/index.html", context=context)


def book_details(request, book_id):
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=book.author_id)
    book_img = os.path.basename(book.image.url)
    print(book_img)
    context = {
        "book": book,
        "image": book_img,
        "author": author
    }
    return render(request, "book/book_info.html", context=context)


def author_info(request, author_id):
    author = Author.objects.get(id=author_id)
    books = author.books()
    context = {
        "author": author,
        "books": books
    }
    return render(request, "book/author.html", context=context)


def home(request):
    return render(request, "book/base.html")


def new_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        print(form["image"].value())
        if form.is_valid():
            book = form.save()
            return redirect("book_details", book_id = book.id)
    else:
        form = BookForm()
    return render(request, "book/book_form.html", context={"form": form})


def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        print(form["image"].value())
        if form.is_valid():
            book = form.save()
            return redirect("book_details", book_id=book.id)
    else:
        form = BookForm(instance=book)
    return render(request, "book/book_form.html", context={"form": form})


def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('/books')
