from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    email = models.EmailField(unique=True, null=True, blank=True)