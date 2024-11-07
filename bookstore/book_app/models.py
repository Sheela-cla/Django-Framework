from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 50,unique = True)

    def __str__(self):
        return self.name


# Create your models here.
class BookInfo(models.Model):
    title = models.CharField(max_length =100,unique=True)
    author = models.CharField(max_length = 50)
    description = models.TextField(max_length=250)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    publication_date = models.DateField(default=None)
    categories = models.ManyToManyField(Category, related_name='bookinfos')
    cover_image = models.ImageField(upload_to='book_covers/',blank=True,null=True)

    def __str__(self):
        return f"{self.title}{self.author}{self.price}"