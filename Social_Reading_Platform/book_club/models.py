from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    pass

class Club:
    name = models.CharField()
    desc = models.CharField()
    visibility = ...
    created_by = ...

class MemberShip:
    user = ...
    club = models.ForeignKey() #Connect this with class club
    is_moderator = ...
    joined_at = models.DateTimeField()

class Book:
    title = models.CharField()
    author = models.CharField()
    chapters = models.IntegerField()
    club = models.ForeignKey() #Connect this with club class

class ClubBook:
    book = models.ForeignKey() #Connect this with Book Class
    club = models.ForeignKey() #Connect this with club class
    is_current = models.BooleanField()

class ReadingProgress:
    user = models.ForeignKey() #Connect this with user field
    club_book = models.ForeignKey() # Connect this with club book
    chapter_number = models.IntegerField()

class Comment:
    user = models.ForeignKey() #Connect this with user 
    chapter = models.IntegerField()
    text = models.CharField()
    timestamp = models.TimeField()
    parent = ...


