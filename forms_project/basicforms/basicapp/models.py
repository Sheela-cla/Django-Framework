from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    text = models.CharField(max_length = 500)

    def __str__(self):
        return f"{self.name}"