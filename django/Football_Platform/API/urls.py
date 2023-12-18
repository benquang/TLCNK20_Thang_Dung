from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('matchs_dataset_model/', views.MatchsDatasetList.as_view(), name='matchs_dataset_model'),
    path('fbref_matchgoals_modified/', views.FbrefMatchgoalsModifiedList.as_view(), name='fbref_matchgoals_modified'),
    path('<str:league>/<str:season>/scores_and_fixtures/', views.Scores_And_Fixtures_List.as_view(), name='scores_and_fixtures'),
    path('scores_and_fixtures/',views.Scores_And_Fixtures_List.as_view(),name='scores_and_fixtures'),
    path('match/<str:match_id>/', views.Matchs_Detail_Infos_View.as_view(), name='match_detail'),
]
