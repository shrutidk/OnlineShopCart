from datetime import datetime
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class Products(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()

    User = get_user_model()
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.id)


class ProductsMeta(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.id)


class Cart(models.Model):

    User = get_user_model()
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):

    quantity = models.IntegerField(default=1, blank=True, null=True)
    cart = models.ForeignKey(Cart, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)



