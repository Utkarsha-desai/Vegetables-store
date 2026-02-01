from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category


# 🏠 Home Page (जर वापरत असशील तर)
def home(request):
    products = Product.objects.filter(is_draft=False)[:8]
    return render(request, 'shop/home.html', {
        'products': products
    })


# 🛍️ Shop Page – All Products
def shop_page(request):
    products = Product.objects.filter(is_draft=False)
    categories = Category.objects.all()

    return render(request, 'shop/shop.html', {
        'products': products,
        'categories': categories
    })


# 📄 Product Details Page
def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_draft=False)

    related_products = Product.objects.filter(
        category=product.category,
        is_draft=False
    ).exclude(id=product.id)[:4]

    return render(request, 'shop/product-details.html', {
        'product': product,
        'related_products': related_products
    })


# ❤️ Wishlist Page (logic नंतर add करू)
from django.shortcuts import render
from .models import Product

def wishlist(request):
    products = Product.objects.filter(is_draft=False)
    return render(request, 'shop/wishlist.html', {'products': products})


# 🛒 Add to Cart (SESSION BASED)
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', [])

    if product_id not in cart:
        cart.append(product_id)

    request.session['cart'] = cart

    # 👉 Add to cart केल्यावर Cart page ला redirect
    return redirect('cart')


# 🧾 Cart Page
def cart_page(request):
    cart = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart)

    return render(request, 'cart/cart.html', {
        'products': products
    })