from django.views.generic import ListView, DetailView, View, CreateView, UpdateView, DeleteView

from catalog.models import Product, Contact
from catalog.forms import ProductForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ContactsView(View):
    template_name = "catalog/contacts.html"

    def get(self, request, *args, **kwargs):
        contact = Contact.objects.first()
        return render(
            request,
            self.template_name,
            {"contact": contact},
        )

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:home")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:home")


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:home")

