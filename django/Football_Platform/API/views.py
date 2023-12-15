from django.shortcuts import render,HttpResponse
from django.http.response import JsonResponse
from rest_framework import status
from .serializers import Matchs_Dataset_Serializer
from .models import MatchsDatasetModel
from API.models import *
from API.serializers import *
from rest_framework.views import APIView
# Create your views here.

def home(request):
    return HttpResponse("HelloWorld")
class Scores_And_Fixtures_List(APIView):
    def get(self, request, league = None,season=None):
        if league and season:
            league = league.replace("_"," ")
            season = season.replace("-","/")
            scores_and_fixtures = View_Scores_And_Fixtures.objects.all().order_by('-match_date',"match_week").filter(league=league,season=season)
            scores_and_fixtures_serializer = View_Scores_And_Fixtures_Serializer(scores_and_fixtures, many=True)
        else:
            scores_and_fixtures = View_Scores_And_Fixtures.objects.all().order_by('-match_date',"match_week")
            scores_and_fixtures_serializer = View_Scores_And_Fixtures_Serializer(scores_and_fixtures, many=True)
        return JsonResponse(scores_and_fixtures_serializer.data, safe=False)

class Matchs_Detail_Infos_View(APIView):
    def get(self, request, match_id = None):
        if match_id:
            matchs_infos = FbrefMatchinfosModified.objects.all().filter(match_id=match_id)
            match_goals = FbrefMatchgoalsModified.objects.all().filter(match_id=match_id)
            match_player_stats = FbrefMatchplayerstatsModified.objects.all().filter(match_id=match_id)
            match_squad = FbrefMatchsquadModified.objects.all().filter(match_id=match_id)
            match_stats = FbrefMatchstatsModified.objects.all().filter(match_id=match_id)
            matchs_infos_serializer = FbrefMatchinfosModified_Serializer(matchs_infos, many=True)
            match_goals_serializer = FbrefMatchgoalsModified_Serializer(match_goals, many=True)
            match_player_stats_serializer = FbrefMatchplayerstatsModified_Serializer(match_player_stats, many=True)
            match_squad_serializer = FbrefMatchsquadModified_Serializer(match_squad, many=True)
            match_stats_serializer = FbrefMatchstatsModified_Serializer(match_stats, many=True)
            data = {
                "matchs_infos":matchs_infos_serializer.data,
                "match_goals":match_goals_serializer.data,
                "match_player_stats":match_player_stats_serializer.data,
                "match_squad":match_squad_serializer.data,
                "match_stats":match_stats_serializer.data,
            }
            return JsonResponse(data, safe=False)
        else:
            matchs_infos = FbrefMatchinfosModified.objects.all()
            matchs_infos_serializer = FbrefMatchinfosModified_Serializer(matchs_infos, many=True)
        return JsonResponse(matchs_infos_serializer.data, safe=False)

class FbrefMatchgoalsModifiedList(APIView):
    def get(self, request):
        match_id = request.GET.get('id')
        team = request.GET.get('team')
        player_name = request.GET.get('player')
        type_goal= request.GET.get('type')
        match_goals = FbrefMatchgoalsModified.objects.all()
        if match_id:
            match_goals = match_goals.filter(match_id=match_id)
        if team:
            match_goals = match_goals.filter(team=team)
        if player_name:
            match_goals = match_goals.filter(player_name=player_name)
        if type_goal:
            match_goals = match_goals.filter(type_of_goal=type_goal)
        match_goals_serializer = FbrefMatchgoalsModified_Serializer(match_goals, many=True)
        return JsonResponse(match_goals_serializer.data, safe=False) 

class MatchsDatasetList(APIView):
    def get(self,request):
        match_id = request.GET.get('id')
        home_team = request.GET.get('home')
        away_team = request.GET.get('away')
        date = request.GET.get('date')
        top_date = request.GET.get('top_date')
        matchs = MatchsDatasetModel.objects.all()
        if match_id:
            matchs = matchs.filter(match_id=match_id)

        if home_team:
            matchs = matchs.filter(home_team=home_team)

        if away_team:
            matchs = matchs.filter(away_team=away_team)

        if date:
            matchs = matchs.filter(match_date=date)

        if top_date:
            sorted_date = matchs.order_by('-match_date')
            matchs = sorted_date[:int(top_date)]

        matchs_serializer = Matchs_Dataset_Serializer(matchs, many=True)
        return JsonResponse(matchs_serializer.data, safe=False)

