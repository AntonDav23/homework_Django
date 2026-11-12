from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    ContactsView,
    HomeView,
    ProductDetailView,
    ProductCreateView,
    ProductDeleteView,
    ProductUpdateView,
    products_by_category,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path("products/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_edit"),
    path(
        "products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path(
        "category/<int:category_id>/",
        products_by_category,
        name="products_by_category_id",
    ),
    path(
        "category/slug/<str:category_slug>/",
        products_by_category,
        name="products_by_category_slug",
    ),
]
