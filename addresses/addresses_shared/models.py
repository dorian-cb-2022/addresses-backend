from django.db import models

class AddressType(models.Model):
    name = models.CharField(max_length=128)
