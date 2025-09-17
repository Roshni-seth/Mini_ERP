from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_view import SupplierViewSet, ProductViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'suppliers', SupplierViewSet)
router.register(r'products', ProductViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
