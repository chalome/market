from django.test import TestCase

from .models import Customer


class CustomerModelTest(TestCase):
    def setUp(self):
        self.user = Customer.objects.create(
            username="chalom",
            email="chalom@gmail.com",
            gender=Customer.Gender.MALE,
            phone="68894773",
            country="Burundi",
            profile_photo="/home/magis/Documents/icons/belle.jpg",
        )

    def test_create_user(self):
        self.assertEqual(self.user.username, "chalom")
        self.assertEqual(self.user.email, "chalom@gmail.com")
        self.assertEqual(self.user.gender, Customer.Gender.MALE)
        self.assertEqual(self.user.phone, "68894773")
        self.assertEqual(self.user.country, "Burundi")
        self.assertEqual(self.user.profile_photo, "/home/magis/Documents/icons/belle.jpg")
        self.assertIsNotNone(self.user.date_joined)
