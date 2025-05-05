from django.contrib import admin

# Register your models here.
from .models import Book, ClubBook

admin.site.register(Book)
admin.site.register(ClubBook)