from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(max_length=50)

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_quantity = models.PositiveIntegerField(max_length=10)
    person = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)