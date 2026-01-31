from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Cart, CartItem, Order, OrderItem
from shop.models import Product
import random
import string

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
    
    if not cart_items.exists():
        messages.warning(request, 'Your cart is empty!')
        return redirect('cart')
    
    if request.method == 'POST':
        # Generate unique order number
        order_number = 'ORD-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        
        # Get form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        apartment = request.POST.get('apartment', '')
        city = request.POST.get('city')
        state = request.POST.get('state')
        postal_code = request.POST.get('postal_code')
        payment_method = request.POST.get('payment_method', 'cod')
        
        # Calculate totals
        subtotal = cart.get_total()
        delivery_fee = 0 if subtotal > 500 else 50
        discount = 0
        total = subtotal + delivery_fee - discount
        
        # Create order
        order = Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            order_number=order_number,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            address=address,
            apartment=apartment,
            city=city,
            state=state,
            postal_code=postal_code,
            subtotal=subtotal,
            delivery_fee=delivery_fee,
            discount=discount,
            total=total,
            payment_method=payment_method,
        )
        
        # Create order items from cart items
        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.product.price
            )
        
        # Clear cart after order placement
        cart.items.all().delete()
        
        messages.success(request, f'Order placed successfully! Your order number is {order_number}')
        return redirect('order-success', order_id=order.id)
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'cart_total': cart.get_total(),
        'cart_count': cart.get_item_count(),
    }
    return render(request, 'cart/checkout.html', context)

def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    context = {
        'order': order,
    }
    return render(request, 'cart/order-success.html', context)
