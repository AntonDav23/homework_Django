from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email","username", "avatar", "phone", "country")


class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("email","username", "avatar", "phone", "country")
