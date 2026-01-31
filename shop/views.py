from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Category, Product


def shop_page(request):
    category = Category.objects.all()
    products = Product.objects.all()
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'category': category,
        'page_obj': page_obj
    }
    return render(request, 'shop/shop.html', context)

def product_details(request, product_id):
    product_details = get_object_or_404(Product, id=product_id)
    ctg = product_details.category
    related_products = Product.objects.filter(category=ctg).exclude(id=product_id)
    context = {
        'product': product_details,
        'related_products': related_products
    }
    return render(request, 'shop/product-details.html', context)

def wishlist(request):
    return render(request, 'shop/wishlist.html')
