from django.urls import path
from .views import RatingViewSet

urlpatterns = [
    path('ratings/', RatingViewSet.as_view({'get': 'list', 'post': 'create'}), name='rating-list'),
    path('ratings/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='rating-detail'),
]
