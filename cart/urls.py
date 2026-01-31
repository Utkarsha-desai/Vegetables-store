from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_page, name='cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add-to-cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove-from-cart'),
    path('update/<int:item_id>/', views.update_cart_item, name='update-cart-item'),
    path('clear/', views.clear_cart, name='clear-cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-success/<int:order_id>/', views.order_success, name='order-success'),
]
