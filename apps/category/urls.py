from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet

app_name = 'category'

router = routers.DefaultRouter()
router.register('', CategoryViewSet, basename='category')

urlpatterns =router.urls
