from django.http import HttpResponse
from django.shortcuts import render
from .models import Tourname
from team.models import Team
from tournament_result.models import TournameResult

def home(request):
    tournaments = Tourname.objects.all()
    teams = Team.objects.all()
    context = {'tournaments': tournaments}
    return render(request, 'tourname/home.html', context=context)

def about_tournament(request, tournament_id):
    tournament = Tourname.objects.get(pk=tournament_id)
    tournament_result = TournameResult.objects.get(pk=tournament_id)
    print(tournament.tourname, "it is here")
    context = {"tournament": tournament}
    return render(request, "tourname/about_tournament.html", context)
