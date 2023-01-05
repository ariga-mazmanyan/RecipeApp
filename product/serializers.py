from rest_framework import serializers
from product.models import Product, Category, Elements, Comments


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ElementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elements
        fields = "__all__"


class CommentSerialize(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('user', 'body')

