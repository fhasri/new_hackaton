# from rest_framework import serializers
# from .models import Order, OrderItem


# class OrderItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderItem
#         fields = '__all__'


# class OrderSerializer(serializers.ModelSerializer):
#     order_items = OrderItemSerializer(many=True, read_only=True)

#     class Meta:
#         model = Order
#         fields = '__all__'

from rest_framework import serializers
from .models import Order, OrderItem
from django_filters import rest_framework as filters

class OrderFilter(filters.FilterSet):
    # Define filters for your model fields
    # Example: filtering by status and created_at
    status = filters.CharFilter(lookup_expr='icontains')
    created_at = filters.DateFilter()

    class Meta:
        model = Order
        fields = ['status', 'created_at']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        exclude = ['order']
        read_only_fields = ['total_cost']


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, write_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['total_cost', 'created_at', 'user', 'updated_at', 'status']

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        total_order_cost = 0

        for order_item_data in order_items_data:
            order_item = OrderItem.objects.create(order=order, **order_item_data)
            total_order_cost += order_item.total_cost

        order.total_cost = total_order_cost
        order.save()
        return order
