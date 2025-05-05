from django.contrib import admin

# Register your models here.
from .models import Club, Membership, Rating

admin.site.register(Club)
admin.site.register(Membership)
admin.site.register(Rating)