from django.db import models
from decimal import Decimal

class Address(models.Model):
    address_name = models.CharField(max_length=256)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, default=Decimal(0.0000000))
    longitude = models.DecimalField(max_digits=10, decimal_places=7, default=Decimal(0.0000000))
