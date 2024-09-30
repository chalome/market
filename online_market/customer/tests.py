from django.test import TestCase
from customer.models import Customer

class TestCustomer(TestCase):
	
	def user_create(self):
		user=Customer.objects.create(
			username='chalome',
			email='chalome@gmail.com',
			gender='Male',
			phone='68894773',
			country='Burundi',
			photo="/home/chalome/Documents/icons/belle.jpg",
			password1='bersha1999',
			password2='bersha1999'
			)
		self.assertEqual(Customer.username, 'chalome')
		self.assertEqual(Customer.email, 'chalome@gmail.com')
		self.assertEqual(Customer.gender, 'Male')
		self.assertEqual(Customer.phone, '68894773')
		self.assertEqual(Customer.password1, 'bersha1999')
		self.assertEqual(Customer.password2, 'bersha1999')

