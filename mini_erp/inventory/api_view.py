from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Supplier, Product, Transaction
from .serializers import SupplierSerializer, ProductSerializer, TransactionSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=["get"])
    def low_stock(self, request):
        low_products = Product.objects.filter(stock__lt=10)
        serializer = self.get_serializer(low_products, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def total_value(self, request):
        total = sum(p.price * p.stock for p in Product.objects.all())
        return Response({"total_inventory_value": total})

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
