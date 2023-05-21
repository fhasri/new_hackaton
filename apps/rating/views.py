from django.shortcuts import render
from rest_framework import filters, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Rating
from .serializers import RatingSerializer
from apps.product.permissions import IsOwnerPermission

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product', 'user']

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsOwnerPermission]
        elif self.action == 'create':
            self.permission_classes = []
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = []
        return super().get_permissions()

