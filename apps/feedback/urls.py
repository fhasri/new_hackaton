# from django.urls import path, include

# urlpatterns = [
#     # Other URL patterns of your project
#     path('feedback/', include('feedback.urls', namespace='feedback')),
# ]
from django.urls import path
from .views import FeedbackViewSet

app_name = 'feedback'

urlpatterns = [
    path('', FeedbackViewSet.as_view({'get': 'list', 'post': 'create'}), name='feedback-list'),
    path('<int:pk>/', FeedbackViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='feedback-detail'),
]
