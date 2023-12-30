from django.db import models
from proprietor.models import Proprietor
from client.models import Client
from product.models import Product


class Cart(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class ClientCart(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)


class ProprietorCart(models.Model):
    proprietor = models.OneToOneField(Proprietor, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
