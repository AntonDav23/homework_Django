from django.core.management.base import BaseCommand
from unicodedata import category

from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Удаляет старые товары и добавляет тестовые товары'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()

        category, created = Category.objects.get_or_create(
            name='Электроника',
            defaults={'description': '"Электронные устройства и бытовая техника'}
        )

        Product.objects.create(
            name='Холодильник',
            description='Двухкамерный холодильник',
            category=category,
            price=37999
        )

        print('Тестовые товары успешно добавлены!')
