from django.urls import path

from cart.views import add_to_cart, cart_page
from . import views

urlpatterns = [
    path('', views.shop_page, name='shop'),
    path('product/<int:product_id>', views.product_details, name='product-details'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('', cart_page, name='cart'),
    path('add/<int:product_id>/', add_to_cart, name='add-to-cart'),
]
