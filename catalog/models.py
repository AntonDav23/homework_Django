from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    slug = models.SlugField(max_length=150, blank=True, verbose_name="Slug")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(
        upload_to="products/",
        verbose_name="Изображение",
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Владелец",
    )
    price = models.IntegerField(verbose_name="Цена")
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликован",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата изменения",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        permissions = [
            ("can_unpublish_product", "Может отменять публикацию товара"),
        ]


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название организации")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Почта")
    address = models.CharField(max_length=255, verbose_name="Адрес")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Контактная информация"
        verbose_name_plural = "Контактная информация"
