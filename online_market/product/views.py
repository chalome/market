from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Category, Product, Purchase
from .serializers import (CategorySerializer, ProductSerializer,
                          PurchaseSerializer)


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(active=True)


class PurchaseViewSet(ModelViewSet):
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()

    @transaction.atomic
    def perform_create(self, serializer):
        # Save the purchase instance
        purchase = serializer.save()

        # Deactivate the product
        product = purchase.product
        product.active = False
        product.save()

        # Optionally return a response with the purchase data
        return Response(serializer.data, status=status.HTTP_201_CREATED)
