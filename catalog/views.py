from catalog.models import Product, Contact
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    products = Product.objects.order_by('-created_at')[:5]

    print(products)
    return render(request, 'catalog/home.html')

def contacts(request):
    contact = Contact.objects.first()

    if request.method == "POST":
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")

    return render(request, 'catalog/contacts.html', {'contact': contact})
