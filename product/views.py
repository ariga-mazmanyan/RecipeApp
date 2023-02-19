from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from product.models import Recipe, Like, Category, Ingredient, UserFollowing, Comment
from product.serializers import (RecipeSerializer,
                                 CommentSerializer,
                                 CategorySerializer,
                                 IngredientSerializer,
                                 FollowingSerializer)
from rest_framework.permissions import IsAuthenticated


class RecipeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        recipe = Recipe.objects.all()

        serializer = RecipeSerializer(recipe, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = RecipeSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(author=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RecipeSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):

        recipe = Recipe.objects.filter(id=pk).first()
        if not recipe:
            return Response({"recipe": "not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = RecipeSerializer(recipe)

        return Response(serializer.data)

    def delete(self, request, pk):
        recipe = Recipe.objects.filter(id=pk, author=request.user)

        if not recipe:
            return Response({"recipe": "not found"}, status=status.HTTP_404_NOT_FOUND)

        recipe.delete()

        return Response(status.HTTP_202_ACCEPTED)


class FollowUnfollow(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        follower_count = UserFollowing.objects.filter(following=pk).count()

        return Response(follower_count, status=status.HTTP_200_OK)

    def post(self, request, pk):
        other_user = User.objects.get(id=pk)

        serializer = FollowingSerializer(data=request.data)
        serializer.is_valid()

        serializer.save(user_id=request.user, following=other_user)

        return Response("Followed", status=status.HTTP_202_ACCEPTED)


class RecipeLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        user = User.objects.get(username=request.user.username)
        recipe = Recipe.objects.get(id=pk)

        new_like = Like(user=user, recipe=recipe)

        recipe.like_count += 1

        recipe.save()
        new_like.save()

        return Response(f"Likes count = {recipe.like_count}", status=status.HTTP_200_OK)


class IngredientView(APIView):

    def post(self, request):

        serializer = IngredientSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class IngredientDetailView(APIView):

    def post(self, request):

        recipe = Recipe.objects.get(id=request.data.get("recipe_id"))
        ingredient = Recipe.objects.get(id=request.data.get("ingredient_id"))

        ingredient = Ingredient(id=ingredient.id, recipe_id=recipe)

        recipe.ingredient_count += 1

        recipe.save()
        ingredient.save()

        return Response(status=status.HTTP_200_OK)


class RecipeCommentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        recipe = Recipe.objects.get(id=pk)
        comment = CommentSerializer(data=request.data)
        comment.is_valid(raise_exception=True)
        recipe.comment_count += 1

        comment.save(author=request.user, recipe_name=recipe)
        recipe.save()

        return Response(status=status.HTTP_202_ACCEPTED)


class CategoryView(APIView):

    def get(self, request):

        category = Category.objects.all()

        serializer = CategorySerializer(category, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = CategorySerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class IngredientView(APIView):

    def get(self, request):
        recipe = Ingredient.objects.all()

        serializer = IngredientSerializer(recipe, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = IngredientSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)






