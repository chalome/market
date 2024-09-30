from django.db import models
from customer.models import Customer

class Category(models.Model):
	name=models.CharField(max_length=255)
	description=models.TextField(blank=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	name=models.CharField(max_length=255)
	category=models.ForeignKey(Category, on_delete=models.CASCADE)
	price=models.PositiveIntegerField()
	photo=models.ImageField(verbose_name='Photo')
	created_by=models.ForeignKey(Customer, on_delete=models.CASCADE)
	description=models.TextField(blank=True)
	created_at=models.DateTimeField(auto_now_add=True)
	active=models.BooleanField(default=True)

	def __str__(self):
		return self.name

class Purchase(models.Model):
	product=models.ForeignKey(Product, on_delete=models.CASCADE)
	purchased_by=models.ForeignKey(Customer, on_delete=models.CASCADE)
	purchased_at=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.product.name