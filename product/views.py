from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from product.models import Product, Likes, Comments
from product.serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated


class ProductView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        products = Product.objects.all()

        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductLikeView(APIView):

    def post(self, request, product_id):

        user = User.objects.get(username=request.user.username)
        product = Product.objects.get(id=product_id)

        new_like = Likes(user=user, post=post)
        new_like.alreadyLiked = True

        product.likes += 1

        product.user_likes.add(user)
        user.liked_posts.add(product)
        product.save()
        new_like.save()
        user.save()

        return Response(status=status.HTTP_200_OK)

    # comment


class ProductSearchView(APIView):

    def get(self, request, element):

        product = Product.objects.filter(elements=element)  # we need a filter class
        if not product:
            return Response({"product": "not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product)

        return Response(serializer.data)

    def delete(self, request, product_name):
        product = Product.objects.filter(name=product_name, user=request.user)

        if not product:
            return Response({"product": "not found"}, status=status.HTTP_404_NOT_FOUND)

        product.delete()

        return Response(status.HTTP_202_ACCEPTED)
