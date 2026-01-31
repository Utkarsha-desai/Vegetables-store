from django.contrib import admin
from .models import Cart, CartItem, Order, OrderItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ('added_at', 'get_subtotal')
    fields = ('product', 'quantity', 'get_subtotal', 'added_at')

    def get_subtotal(self, obj):
        return f"₹{obj.get_subtotal()}"
    get_subtotal.short_description = 'Subtotal'

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'session_key', 'get_item_count', 'get_total', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('user__username', 'session_key')
    readonly_fields = ('created_at', 'updated_at', 'get_total', 'get_item_count')
    inlines = [CartItemInline]

    def get_total(self, obj):
        return f"₹{obj.get_total()}"
    get_total.short_description = 'Total'

    def get_item_count(self, obj):
        return obj.get_item_count()
    get_item_count.short_description = 'Items'

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'quantity', 'get_subtotal', 'added_at')
    list_filter = ('added_at',)
    search_fields = ('product__name', 'cart__user__username')
    readonly_fields = ('added_at', 'get_subtotal')

    def get_subtotal(self, obj):
        return f"₹{obj.get_subtotal()}"
    get_subtotal.short_description = 'Subtotal'


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('get_subtotal',)

    def get_subtotal(self, obj):
        return f"₹{obj.get_subtotal()}"
    get_subtotal.short_description = 'Subtotal'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'user', 'first_name', 'last_name', 'email', 'total', 'status', 'payment_method', 'created_at')
    list_filter = ('status', 'payment_method', 'created_at')
    search_fields = ('order_number', 'email', 'first_name', 'last_name', 'user__username')
    readonly_fields = ('order_number', 'created_at', 'updated_at')
    inlines = [OrderItemInline]
    fieldsets = (
        ('Order Information', {
            'fields': ('order_number', 'user', 'status', 'payment_method')
        }),
        ('Customer Details', {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),
        ('Shipping Address', {
            'fields': ('address', 'apartment', 'city', 'state', 'postal_code')
        }),
        ('Pricing', {
            'fields': ('subtotal', 'delivery_fee', 'discount', 'total')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price', 'get_item_subtotal')
    list_filter = ('order__created_at',)
    search_fields = ('order__order_number', 'product__name')
    readonly_fields = ('get_item_subtotal',)

    def get_item_subtotal(self, obj):
        return f"₹{obj.get_subtotal()}"
    get_item_subtotal.short_description = 'Subtotal'
