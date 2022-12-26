from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    elements = models.ManyToManyField("Elements")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # likes (the count)
    # comments (the count)


class Category(models.Model):
    cuisine = models.CharField(max_length=50)


class Elements(models.Model):
    elements = models.CharField(max_length=50)


class Likes(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    like_count = models.IntegerField()

