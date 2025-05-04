from django.db import models

# Create your models here.
from apps.users.models import Users

class Club(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    visibility = models.BooleanField(default=False)
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Membership(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    is_moderator = models.BooleanField(default=False)
    joined_at = models.DateTimeField(auto_now_add=True)

