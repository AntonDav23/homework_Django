from django.views.generic import ListView, DetailView, View

from catalog.models import Product, Contact
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


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
        return render(request, self.template_name,{"contact": contact},)


    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
