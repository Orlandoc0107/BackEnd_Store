from django.contrib.auth.models import User
from django.db import models


class Proprietor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True)
    dni = models.CharField(max_length=255, null=True, blank=True, unique=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    website = models.URLField()
    phone = models.CharField(max_length=255, null=True, blank=True, unique=True)
    ask = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
