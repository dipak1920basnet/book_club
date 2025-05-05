from django.db import models

# Create your models here.
from apps.users.models import Users
from apps.clubs.models import Club

class UnMatchedAuthor(Exception):
    pass

class Book(models.Model):
    
    title = models.CharField(max_length=64)
    chapters = models.IntegerField()
    author = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, blank=True)
    # Even though user delets account The books should not be deleted 
    # might considering changing models.cascade
    name_copy = models.CharField(max_length=400)

    def save(self, *args, **kwargs):
        if self.author:
            full_name = self.author.get_full_name() or self.author.username
            if not self.name_copy:
                self.name_copy = full_name
            elif self.name_copy != full_name:
                raise UnMatchedAuthor("The copy of authoer name should be matched")
        super().save(*args, **kwargs)

class ClubBook(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    is_current = models.BooleanField(default=False)

