from rest_framework import serializers
from product.models import Recipe, Category, Ingredient, Comment, UserFollowing
from django.contrib.auth import get_user_model
User = get_user_model()


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ElementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'body')


class FollowingSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserFollowing
        fields = "__all__"


class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

    # def get_following(self, obj):
    #     return FollowingSerializer(obj.following.all(), many=True).data
    #
    # def get_followers(self, obj):
    #     return FollowersSerializer(obj.followers.all(), many=True).data

