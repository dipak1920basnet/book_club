from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Users(AbstractUser):
    email = models.EmailField(unique=True, null=True, blank=True)