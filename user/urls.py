from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_user, name="logout"),

]
