from django.urls import path
from .views import index, book_details, author_info, new_book, edit_book, delete_book

urlpatterns = [
    path('', index),
    path('<int:book_id>', book_details, name="book_details"),
    path('<int:book_id>/edit', edit_book, name="book_edit"),
    path('<int:book_id>/delete', delete_book),
    path('author/<int:author_id>', author_info),
    path('new', new_book),
]
