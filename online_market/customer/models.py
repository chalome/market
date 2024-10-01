from django.contrib.auth.models import AbstractUser
from django.db import models


class Customer(AbstractUser):
    class Gender(models.TextChoices):
        MALE = "MALE", "Male"
        FEMALE = "FEMALE", "Female"

    profile_photo = models.ImageField(verbose_name="Profile picture")
    gender = models.CharField(max_length=10, choices=Gender.choices, verbose_name="Gender")
    phone = models.CharField(max_length=20, verbose_name="Your Phone Number")
    country = models.CharField(max_length=20)
    date_joined = models.DateTimeField(auto_now_add=True)
