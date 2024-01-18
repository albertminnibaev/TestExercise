from django.urls import path, include
from rest_framework.routers import DefaultRouter

from net.apps import NetConfig
from net.views import NetViewSet, ProductViewSet

app_name = NetConfig.name


net_router = DefaultRouter()
net_router.register(r'net', NetViewSet, basename='net')
product_router = DefaultRouter()
product_router.register(r'product', ProductViewSet, basename='product')


urlpatterns = [
    path('', include(net_router.urls)),
    path('', include(product_router.urls)),
]
