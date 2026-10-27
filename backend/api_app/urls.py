from django.urls import path
from .views import users, create, user_fun

urlpatterns = [
    path('users/', users, name="users"),
    path('users/create/', create, name="create"),
    path('users/user_fun/<int:pk>', user_fun, name="user_fun"),

]