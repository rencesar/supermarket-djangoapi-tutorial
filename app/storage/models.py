import uuid

from django.db import models


class Section(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50)
    max_allowed_items = models.IntegerField(verbose_name="Max allowed items")
    description = models.TextField(verbose_name="Description")
    temperature = models.IntegerField(verbose_name="Temperature", default=25)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(verbose_name="Name", max_length=150)
    price = models.FloatField(verbose_name="Price")
    barcode = models.UUIDField(verbose_name="BarCode", default=uuid.uuid4)
    brand = models.CharField(verbose_name="Brand", max_length=50)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, related_name="products", null=True, blank=True)
    stock_available = models.IntegerField(verbose_name="Stock available", default=0)

    def __str__(self):
        return self.name
