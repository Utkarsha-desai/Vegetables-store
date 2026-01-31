def cart_context(request):
    """Add cart information to all templates"""
    from cart.models import Cart
    
    cart_count = 0
    
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            cart_count = cart.get_item_count()
        except Cart.DoesNotExist:
            cart_count = 0
    else:
        if request.session.session_key:
            try:
                cart = Cart.objects.get(session_key=request.session.session_key)
                cart_count = cart.get_item_count()
            except Cart.DoesNotExist:
                cart_count = 0
    
    return {
        'cart_count': cart_count
    }
