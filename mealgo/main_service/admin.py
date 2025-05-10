from django.contrib import admin
from .models import User, Category, Food, Cart, CartItem, Order, OrderItem, Rating

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Food)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Rating)
