from django.urls import path
from .views import users, create, user_fun, register, login, user_profile
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('users/', users, name="users"),
    path('users/create/', create, name="create"),
    path('user_fun/<int:pk>', user_fun, name="user_fun"),
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('user_profile/', user_profile, name="user_profile"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]