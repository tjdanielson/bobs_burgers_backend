from django.db import models
from django.contrib.auth.models import User
from menu.models import Menu

# Create your models here.
class Order(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField()

class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
