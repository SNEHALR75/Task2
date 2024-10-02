from django.db import models


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    expire_date = models.DateField()
    manufacturing_date = models.DateField()
