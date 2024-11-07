from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=264,unique=True)
    last_name = models.CharField(max_length=264,unique=True)
    email = models.EmailField(max_length=264)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"
         

