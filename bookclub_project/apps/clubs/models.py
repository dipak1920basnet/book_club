from django.db import models

# Create your models here.
from apps.users.models import Users
from django.core.validators import MaxValueValidator, MinValueValidator

class Club(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    visibility = models.BooleanField(default=False)
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"name: {self.name}"


class Membership(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    is_moderator = models.BooleanField(default=False)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"
    
class Rating(models.Model):
    club_name = models.ForeignKey(Club, on_delete=models.CASCADE, null=True, blank=True)
    club_rating = models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)],
        default=0
    )