
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='Itech',
        default_version='v1',
        description='API for online Marketplace',
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/product/', include('apps.product.urls')),
    path('api/v1/category/', include('apps.category.urls', namespace='category')),
    path('api/v1/account/', include('apps.account.urls')),
    path('api/v1/comment/', include('apps.comment.urls')),
    path('api/v1/order/', include('apps.order.urls')),
    path('api/v1/feedback/', include('apps.feedback.urls')),
    path('api/v1/payment/', include('apps.payment.urls')),
    path('docs/', schema_view.with_ui('swagger')),
]
