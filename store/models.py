from django.db import models

# Create your models here.


class Store (models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    website = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True, unique=True)

