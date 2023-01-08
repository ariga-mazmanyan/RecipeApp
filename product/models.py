from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(max_length=100, unique=True, primary_key=True)
    username = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    followers = models.ManyToManyField('self', related_name='follower', blank=True)
    following = models.ManyToManyField('self', related_name='following', blank=True)


class Recipe(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    ingredient = models.ManyToManyField("Elements")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like_count = models.PositiveIntegerField(default=0)
    comments = models.ForeignKey("Comments", on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    cuisine = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class UserFollowing(models.Model):
    user_id = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    following_user_id = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.user_id} follows {self.following_user_id}"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} liked {self.recipe}"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
