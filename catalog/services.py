from catalog.models import Product, Category
from django.core.cache import cache


def get_products_by_category(category_id=None, category_slug=None):
    if category_id:
        category = Category.objects.get(id=category_id)
    elif category_slug:
        category = Category.objects.get(slug=category_slug)
    else:
        return Product.objects.none()

    cache_key = f"category_{category.id}"
    products = cache.get(cache_key)
    if products is None:
        products = list(Product.objects.filter(category=category))
        cache.set(cache_key, products, 60 * 15)
    return products
