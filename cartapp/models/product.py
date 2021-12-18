from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200)
    # image = models.ImageField(upload_to='products/')

    # relational field
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
