from django.db import models

# Create your models here.
from apps.users.models import Users
from apps.books.models import ClubBook

class ReadingProgress(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    club_book = models.ForeignKey(ClubBook, on_delete=models.CASCADE)
    chapter_number = models.IntegerField()

