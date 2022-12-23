from decimal import Decimal
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.utils import tree
import datetime


class User(AbstractUser):
    pass


print("here")


class Product(models.Model):
    title = models.CharField(max_length=64, null=False)
    category = models.CharField(max_length=64,)
    description = models.CharField(max_length=255,)
    sb = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, default=00.00)
    date = models.DateField(default=datetime.datetime.now())
    url = models.CharField(max_length=255, default="")
    user = models.ManyToManyField(User, blank=True, related_name="product")
    creator = models.CharField(max_length=64, default="")
    status = models.CharField(max_length=64, default="available")
    win = models.CharField(max_length=64, default=False)
    winner = models.CharField(max_length=64, blank='')

    def __str__(self):
        return f"{self.title}"


print("here0")


class Reviews(models.Model):
    comment = models.TextField(null=False)
    rate = models.IntegerField(null=False)
    user = models.ForeignKey(User, on_delete=CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="comments", default="")
    username = models.CharField(max_length=64, default="")

    def __str__(self):
        return f"{self.comment} -{self.rate}-{self.user}"


print("here1")


class Bid(models.Model):
    bid = models.DecimalField(
        max_digits=8, decimal_places=2, null=False, default=00.00)
    user = models.ForeignKey(User, on_delete=CASCADE,
                             default="", editable=False)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="bids", default="")
    username = models.CharField(max_length=64, default="")

    def __str__(self):
        return f"{self.bid}{self.username}"


print("here3")
