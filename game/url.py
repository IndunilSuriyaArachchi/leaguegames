from django.urls import path
from . import views


urlpatterns = [
    path('team/',views.team_list),
    path('team/<int:pk>/',views.team_details),
    path('team/add/',views.team_add),
    path('game/',views.game_list),
    path('game/<int:pk>/',views.game_details),
    path('game/<int:pk>/player/',views.game_play_details),
    path('game/selectplayers/',views.select_players),
    path('player/',views.players_list),
    path('player/<int:pk>/',views.player_details),
    
]