from rest_framework import serializers
from .models import User, Category, Food, Cart, CartItem, Order, OrderItem, Rating


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'address', 'first_name', 'last_name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class FoodSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Food
        fields = ['id', 'name', 'description', 'price', 'category', 'image']


class CartItemSerializer(serializers.ModelSerializer):
    food = FoodSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'food', 'quantity', 'subtotal']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.DecimalField(source='total_price', read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_price']


class OrderItemSerializer(serializers.ModelSerializer):
    food = FoodSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'food', 'quantity', 'price', 'subtotal']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.DecimalField(source='final_price', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'created_at', 'final_price', 'items', 'total_price']


class RatingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    food = FoodSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = ['id', 'user', 'food', 'score', 'comment', 'created_at', 'is_positive']
