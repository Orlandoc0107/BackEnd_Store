from django.db import models
from store.models import Store


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Photo(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_photos')
    image = models.ImageField(upload_to='product_images/')


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(null=True, blank=True)
    code = models.IntegerField(null=True, blank=True)
    is_available = models.BooleanField(default=False)
    quantity = models.IntegerField(null=True, blank=True)
    on_sale = models.BooleanField(default=False)
    brand = models.CharField(max_length=255, null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    origin = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    photos = models.ManyToManyField(Photo, related_name='product_photos')  # Cambiado aquí
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
