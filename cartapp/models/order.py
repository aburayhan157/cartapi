import datetime
from django.contrib.auth.models import User
from django.db import models
from .product import Product


class Order(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=11, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
