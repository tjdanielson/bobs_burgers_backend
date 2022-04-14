from django.db import models

# Create your models here.
class Menu(models.Model):
    item = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
