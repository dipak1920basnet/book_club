from django.db import models

# Create your models here.
from apps.users.models import Users
from apps.books.models import  ClubBook

class Comment(models.Model):
    user = models.ForeignKey(on_delete=models.CASCADE)
    club_book = models.ForeignKey(ClubBook, on_delete=models.CASCADE)
    chapter = models.IntegerField()
    text = models.CharField(max_length=600)
    timestamp = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self',null=True,blank=True, on_delete=models.CASCADE)
    upvote = models.ManyToManyField(Users, related_name='comment_upvotes', blank=True)