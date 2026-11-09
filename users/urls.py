from django.urls import path
from users.views import RegisterView, CustomLoginView, ProfileUpdateView
from django.contrib.auth.views import LogoutView

app_name = "users"
urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", ProfileUpdateView.as_view(), name="profile"),
]
