from django.db import models

# Create your models here.
class Burgers(models.Model):
    name = models.CharField(max_length=500)
    img = models.ImageField()
    date = models.DateField()
