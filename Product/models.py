from django.db import models
from OnlineCartApp.models import ProductsMeta
from django.contrib.auth import get_user_model

# Create your models here.


class Orders(models.Model):

    subtotal = models.IntegerField(default=None, blank=True)
    tax = models.IntegerField(default=None, blank=True)
    total = models.IntegerField(default=None, blank=True)
    User = get_user_model()
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


class OrderItem(models.Model):

    quantity = models.IntegerField()
    price = models.IntegerField()
    order = models.ForeignKey(Orders, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductsMeta, null=True, on_delete=models.CASCADE)






