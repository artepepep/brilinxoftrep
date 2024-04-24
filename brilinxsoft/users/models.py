from django.contrib.auth.models import AbstractUser
from django.db import models
from .choices import DEVELOPER_CHOICES

class UserModel(AbstractUser):
    name = models.CharField(max_length=105)
    dev_role = models.CharField(max_length=55, choices=DEVELOPER_CHOICES)

    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions')
