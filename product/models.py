from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    elements = models.ForeignKey("Elements", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    user_likes = models.ManyToManyField(User)
    # comments (the count)


class Category(models.Model):
    cuisine = models.CharField(max_length=50)


class Elements(models.Model):
    elements = models.CharField(max_length=50)


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    like_count = models.IntegerField()
    alreadyLiked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} liked {self.post}"


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.user}"
