from rest_framework.serializers import ModelSerializer
from product.models import *
from customer.models import Customer

class CategorySerializer(ModelSerializer):
	class Meta:
		model=Category
		fields='__all__'

class ProductSerializer(ModelSerializer):
	class Meta:
		model=Product
		fields='__all__'
		
class PurchaseSerializer(ModelSerializer):
	class Meta:
		model=Purchase
		fields='__all__'
