from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from users.forms import CustomUserCreationForm, CustomUserUpdateForm
from users.models import CustomUser
from django.core.mail import send_mail
from django.conf import settings


class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        response = super().form_valid(form)

        send_mail(
            subject="Добро пожаловать в SkyStore!",
            message=f"Здравствуйте, {self.object.username}! Вы успешно зарегистрировались.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[self.object.email],
        )
        return response


class CustomLoginView(LoginView):
    template_name = "users/login.html"


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = CustomUserUpdateForm
    template_name = "users/profile.html"
    success_url = reverse_lazy("users:profile")

    def get_object(self):
        return self.request.user
