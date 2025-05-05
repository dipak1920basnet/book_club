from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Club

class ClubExistsError(Exception):
    pass
# Create your views here.
def club_list(request):
    clublist = Club.objects.all()
    return render(request, "clublist.html",
                  {
                    "clublist":clublist
                  })

@login_required
def my_club(request):
    return HttpResponse("<h1>Feature arriving Soon</h1>")
    
@login_required
def create_club(request):
    if request.method == "POST":
        club_name = request.POST.get("club-name")
        club_description = request.POST.get("club-description")
        club_visibility = request.POST.get("club-privacy")

        if club_visibility == "public":
            visible = True 
        else:
            visible = False # The club is private

        # Check if clubname exists
        club_name = Club.objects.filter(name=club_name).exists()
        if club_name:
            return render(request, "create_club.html",
                          {"error_message":"Club already exists"}
                          )
        
        new_club = Club.objects.create(name=club_name, desc=club_description, visibility = visible, created_by=request.user)
        new_club.save()
        return redirect("clubs:my_club")

    return render(request, "create_club.html")