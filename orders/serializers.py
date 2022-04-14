from rest_framework import serializers
from django.contrib.auth.models import User
from menu.models import Menu
from .models import Order, OrderLine

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'item']

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'date', 'total', 'user']

class OrderLineSerializer(serializers.ModelSerializer):
    menu_item = MenuSerializer(read_only=True)
    order = OrderSerializer(read_only=True)
    class Meta:
        model = OrderLine
        fields = ['id', 'menu_item', 'order']