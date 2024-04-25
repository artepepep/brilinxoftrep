from django.contrib.auth.models import AbstractUser
from django.db import models
from .choices import DEVELOPER_CHOICES

class Users(AbstractUser):
    dev_role = models.CharField(max_length=55, choices=DEVELOPER_CHOICES)
