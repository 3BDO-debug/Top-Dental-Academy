from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=350, verbose_name="Book Name")
    category = models.CharField(max_length=350, verbose_name="Book's Category")
    author = models.CharField(max_length=350, verbose_name="Book Author")
    content = models.FileField(verbose_name="Book File ex:book.pdf")
    short_desc = models.CharField(max_length=350, verbose_name="Book's Short Description")
    book_thumbnail = models.ImageField(verbose_name="Book Thumbnail")
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(verbose_name="Book Price")
    is_downloadable = models.BooleanField(verbose_name="Can Be Downlaoded")

    def __str__(self):
        return self.name