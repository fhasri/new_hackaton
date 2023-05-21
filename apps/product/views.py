# from rest_framework import filters, viewsets
# from django_filters.rest_framework import DjangoFilterBackend
# from .permissions import IsAdminOrActivePermission, IsOwnerPermission
# from .models import Product, ProductImage
# from .serializers import ProductSerializer, ProductImageSerializer

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_fields = ['category', 'author']
#     search_fields = ['title']
#     ordering_fields = ['created_at', 'title']

#     def get_permissions(self):
#         if self.action in ['update', 'destroy', 'partial_update']:
#             self.permission_classes = [IsOwnerPermission]
#         elif self.action == 'create':
#             self.permission_classes = [IsAdminOrActivePermission]
#         elif self.action in ['list', 'retrieve']:
#             self.permission_classes = []
#         return super().get_permissions()

# class ProductImageViewSet(viewsets.ModelViewSet):
#     queryset = ProductImage.objects.all()
#     serializer_class = ProductImageSerializer

#     def get_permissions(self):
#         if self.action in ['create', 'update', 'partial_update', 'destroy']:
#             self.permission_classes = [IsOwnerPermission]
#         elif self.action in ['list', 'retrieve']:
#             self.permission_classes = []
#         return super().get_permissions()

from rest_framework import filters, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsAdminOrActivePermission, IsOwnerPermission
from .models import Product, ProductImage
from .serializers import ProductSerializer, ProductImageSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'author']
    search_fields = ['name']
    ordering_fields = ['created_at', 'name']

    def get_permissions(self):
        if self.action in ['update', 'destroy', 'partial_update']:
            self.permission_classes = [IsOwnerPermission]
        elif self.action == 'create':
            self.permission_classes = [IsAdminOrActivePermission]
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = []
        return super().get_permissions()

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsOwnerPermission]
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = []
        return super().get_permissions()

