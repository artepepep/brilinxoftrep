from django.contrib.auth.models import AbstractUser
from django.db import models
from .choices import DEVELOPER_CHOICES, ADMIN_CHOICES

class Users(AbstractUser):
    email = models.EmailField(max_length=254)
    dev_role = models.CharField(max_length=55, choices=DEVELOPER_CHOICES)
    admin_role = models.CharField(max_length=55, choices=ADMIN_CHOICES)
