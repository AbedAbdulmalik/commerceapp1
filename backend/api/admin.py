from django.contrib import admin
from .models import Customer, Product, Order, OrderItem, CartItem

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(CartItem)