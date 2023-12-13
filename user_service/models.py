
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

from django.contrib.auth.models import PermissionsMixin
# Create your models here.

Roles = (
    ('student', 'student'),
    ('staff', 'staff'),
    ('editor', 'editor'),
    ('admin', 'admin'),
)

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    number = models.CharField(unique=True, max_length=15)
    roles = models.CharField(max_length=10,null=False,blank=False,choices=Roles)

    is_active = models.BooleanField(blank=False, null=False, default=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)