from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from users.serializers import UserSerializer


class UserListCreateView(APIView):
    user_queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        serializer = self.serializer_class(self.user_queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(is_active=True)

        return Response(serializer.data)


class UserRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
