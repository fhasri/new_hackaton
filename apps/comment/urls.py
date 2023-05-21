from django.urls import path
from .views import CommentViewSet

app_name = 'comment'

urlpatterns = [
    path('', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list'),
    path('<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='comment-detail'),
]

