from django.db import models
#from multiselectfield import MultiSelectField


# Create your models here.

from django.db import models

class Car(models.Model):
    location_choices = (
        ('alvik','ALVIK'),
        ('axelsberg','AXELSBERG'),
        ('akalla','AKALLA'),
        ('sickla','SICKLA'),
        ('ropsten','ROPSTEN'),
        ('vällingby','VÄLLINGBY'),
        ('solna','SOLNA'),
        ('barkarby','BARKARBY'),
        ('stockholmcity','STOCKHOLMCITY')
    )
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)
    location = models.CharField(max_length=50, choices=location_choices, default='STOCKHOLMCITY')
    miles = models.IntegerField()
    passengers = models.IntegerField()
    no_of_owners = models.CharField(max_length=100)
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    color = models.CharField(max_length=100)

    def __str__(self):
        return f" {self.make} {self.model} {self.year} {self.color} {self.fuel_type}"
