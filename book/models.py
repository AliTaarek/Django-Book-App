from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)

    def books(self):
        return self.book_set.all()

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100, unique=True)
    publish_date = models.DateField()
    added_at = models.DateTimeField(auto_now_add=True)
    price = models.BigIntegerField()
    image = models.FileField(upload_to='book/static/book/images/', default='book/static/book/images/img.jpg')
    appropriate = models.CharField(max_length=20, choices=[("For kids", "Under 8"), ("For Teens", "8 - 15"),
                                                           ("For Adults", "+15")], default="For Teens")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("book_details", args=[self.id])



