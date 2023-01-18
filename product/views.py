from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from recipe_app.product.models import Recipe, Like
from recipe_app.product.serializers import RecipeSerializer, FollowingSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated


class RecipeView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        recipe = Recipe.objects.all()

        serializer = RecipeSerializer(recipe, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = RecipeSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RecipeSearchView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk):

        recipe = Recipe.objects.filter(ingredient=pk)
        if not recipe:
            return Response({"recipe": "not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = RecipeSerializer(recipe)

        return Response(serializer.data)

    def delete(self, request, pk):
        recipe = Recipe.objects.filter(name=pk, user=request.user)

        if not recipe:
            return Response({"recipe": "not found"}, status=status.HTTP_404_NOT_FOUND)

        recipe.delete()

        return Response(status.HTTP_202_ACCEPTED)


class FollowUnfollow(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        user = User.objects.get(user_id=self.request.data.get("user_id"))
        following_data = FollowingSerializer(user.following.all(), many=True)

        return Response(following_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        user = User.objects.get(user_id=self.request.data.get("user_id"))
        other_user = User.objects.get(user_id=self.request.data.get("follow"))
        req_type = request.data.get("type")

        if req_type == "follow":
            user.following.add(other_user)
            other_user.followers.add(user)
            return Response("Following", status=status.HTTP_200_OK)

        elif req_type == "unfollow":
            user.following.remove(other_user)
            other_user.followers.remove(user)
            return Response("Unfollowed", status=status.HTTP_200_OK)


class RecipeLikeView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, recipe_id):

        user = User.objects.get(username=request.user.username)
        recipe = Recipe.objects.get(id=recipe_id)

        new_like = Like(user=user, recipe=recipe)

        recipe.likes += 1

        recipe.user_likes.add(user)
        user.liked_posts.add(recipe)
        recipe.save()
        new_like.save()
        user.save()

        return Response(status=status.HTTP_200_OK)


class RecipeCommentView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, product_id):

        recipe = Recipe.objects.get(id=product_id)
        comment = CommentSerializer(data=request.POST)
        comment.is_valid(raise_exception=True)
        comment.recipe = recipe
        comment.save()

        return Response(status=status.HTTP_202_ACCEPTED)
