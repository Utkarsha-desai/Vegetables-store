from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .models import Cart, CartItem
from shop.models import Product

def get_or_create_cart(request):
    """Get or create cart for the current user/session"""
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        if not request.session.session_key:
            request.session.create()
        session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key)
    return cart

def cart_page(request):
    cart = get_or_create_cart(request)
    cart_items = cart.items.all()
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'cart_total': cart.get_total(),
        'cart_count': cart.get_item_count(),
    }
    return render(request, 'cart/cart.html', context)

def add_to_cart(request, product_id):
    """Add product to cart"""
    product = get_object_or_404(Product, id=product_id)
    cart = get_or_create_cart(request)
    
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': 1}
    )
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f'{product.name} quantity updated in cart!')
    else:
        messages.success(request, f'{product.name} added to cart!')
    
    # Redirect to the page they came from or to shop page
    next_url = request.GET.get('next', 'shop')
    return redirect(next_url)

def remove_from_cart(request, item_id):
    """Remove item from cart"""
    cart = get_or_create_cart(request)
    cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
    product_name = cart_item.product.name
    cart_item.delete()
    messages.success(request, f'{product_name} removed from cart!')
    return redirect('cart')

def update_cart_item(request, item_id):
    """Update cart item quantity"""
    if request.method == 'POST':
        cart = get_or_create_cart(request)
        cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
        
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, 'Cart updated successfully!')
        else:
            cart_item.delete()
            messages.success(request, 'Item removed from cart!')
    
    return redirect('cart')

def clear_cart(request):
    """Clear all items from cart"""
    cart = get_or_create_cart(request)
    cart.items.all().delete()
    messages.success(request, 'Cart cleared successfully!')
    return redirect('cart')

def checkout(request):
    cart = get_or_create_cart(request)
    cart_items = cart.items.all()
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'cart_total': cart.get_total(),
        'cart_count': cart.get_item_count(),
    }
    return render(request, 'cart/checkout.html', context)
