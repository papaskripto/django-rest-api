from django.db import models

# Book model
class Book (models.Model):
    book_title = models.CharField (max_length=100)
    author = models.CharField (max_length=40)
    date_added = models.DateTimeField (auto_now_add=True)

def __str__ (self):
    return f'{self.book_title}, {self.author}, {self.date_added}'
