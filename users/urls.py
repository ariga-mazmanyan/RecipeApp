from django.urls import path
from users.views import user_views

urlpatterns = [
    path("", user_views.UserListCreateView.as_view()),
    path("<int:pk>/", user_views.UserRetrieveUpdateView.as_view()),
]