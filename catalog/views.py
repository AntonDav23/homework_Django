from catalog.models import Product, Contact
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def home(request):
    products = Product.objects.all()

    return render(request, "catalog/home.html", {"products": products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "catalog/product_detail.html", {"product": product})


def contacts(request):
    contact = Contact.objects.first()

    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")

    return render(request, "catalog/contacts.html", {"contact": contact})
