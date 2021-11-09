from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length = 1000 , null = True , blank = True)
    price = models.FloatField(null = True , blank = True)
    image = models.ImageField(upload_to="image", null = True , blank = True)
    description = models.TextField(null = True , blank = True)

    def __str__(self):
        return self.book_name