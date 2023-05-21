# from django.shortcuts import render

# from rest_framework import viewsets, permissions
# from rest_framework.decorators import action
# from rest_framework.response import Response

# from .models import Order, OrderStatus
# from .serializers import OrderSerializer


# class OrderViewSet(viewsets.ModelViewSet):
#     serializer_class = OrderSerializer

#     def get_queryset(self):
#         return Order.objects.filter(user=self.request.user)

#     @action(methods=['GET'], detail=True)
#     def confirm(self, request, pk):
#         order = self.get_object()
#         order.status = OrderStatus.in_process
#         order.save()
#         return Response({'message': 'Order is in process'}, status=200)

#     def get_permissions(self):
#         if self.action == 'confirm':
#             self.permission_classes = [permissions.AllowAny]
#         else:
#             self.permission_classes = [permissions.IsAuthenticated]
#         return super().get_permissions()

from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Order, OrderStatus
from .serializers import OrderSerializer, OrderFilter
from rest_framework.response import Response
from rest_framework.decorators import action



class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = OrderFilter
    search_fields = ['user__username', 'address']  # Define fields to search

    def get_permissions(self):
        if self.action == 'confirm':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()

    @action(methods=['GET'], detail=True)
    def confirm(self, request, pk):
        order = self.get_object()
        order.status = OrderStatus.in_process
        order.save()
        return Response({'message': 'Order is in process'}, status=200)

    # ... Implement other actions, such as create, update, delete
