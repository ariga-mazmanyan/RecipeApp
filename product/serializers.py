from rest_framework import serializers
from product.models import Recipe, Category, Ingredient, Comment, UserFollowing


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
        fields = "__all__"


class FollowingSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserFollowing
        fields = "__all__"


class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = "__all__"


