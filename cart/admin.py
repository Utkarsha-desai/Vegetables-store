from django.contrib import admin
from .models import Cart, CartItem

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
