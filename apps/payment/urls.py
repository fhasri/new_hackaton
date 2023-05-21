# from django.urls import include, path
# from rest_framework.routers import DefaultRouter
# from .views import PaymentMethodViewSet, TransactionViewSet

# router = DefaultRouter()
# router.register(r'payment-methods', PaymentMethodViewSet)
# router.register(r'transactions', TransactionViewSet)

# urlpatterns = [
#     # Other URL patterns of your project
#     path('api/', include(router.urls)),
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentMethodViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'payment-methods', PaymentMethodViewSet, basename='payment-method')
router.register(r'transactions', TransactionViewSet, basename='transaction')

urlpatterns = [
    # Other URL patterns of your project
    path('api/', include(router.urls)),
]
