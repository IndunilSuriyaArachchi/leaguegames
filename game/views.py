from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import permission_classes

@api_view()
def team_list(request):
    permission_classes = [permissions.IsAdminUser]
    queryset=Team.objects.prefetch_related('player_set').select_related('coach').all()
    serializer=TeamSerializer(
        queryset, many=True, context={'request':request}
    )
    
    return Response (serializer.data)

@api_view()
def players_list(request):
    permission_classes = [permissions.IsAdminUser]
    queryset = Player.objects.all()
    serializer = PlayerSerializer(
        queryset, many=True, context={'request':request}
    )
    return Response (serializer.data)

@api_view()
def player_details(request, pk):
    player= get_object_or_404(Player,pk=pk)
    serializer = PlayerSerializer(player)
    permission_classes = [permissions.IsAuthenticated]
    return Response (serializer.data)

@api_view()
def team_details(request, pk):
    team= get_object_or_404(Team,pk=pk)
    serializer = TeamSerializer(team)
    permission_classes = [permissions.IsAdminUser]
    return Response (serializer.data)

@api_view()
def game_list(request):
    queryset = Game.objects.all()
    serializer = GameSerializer(
        queryset, many=True, context={'request':request}
    )
    permission_classes = [permissions.IsAuthenticated]
    return Response (serializer.data)

@api_view()
def game_details(request, pk):
    queryset=GameTeam.objects.all()
    serializer=GameTeamSerialier(
        queryset, many=True, context={'request':request, 'game_id':pk}
    )
    permission_classes = [permissions.IsAuthenticated]
    return Response (serializer.data)

@api_view()
def game_play_details(request, pk):
    queryset=GamePlayTeam.objects.all()
    serializer=GamePlayTeamSerializer(
        queryset, many=True, context={'request':request, 'game_id':pk}
    )
    permission_classes = [permissions.IsAdminUser]
    return Response (serializer.data)
             
@api_view(['POST'])
def select_players(request):
    serializer = GamePlayTeamSerializer (data=request.data)
    permission_classes = [permissions.IsAdminUser]
    if serializer.is_valid():
        #serializer.validated_data
        serializer.save()
        return Response (serializer.data, status=201)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def team_add(request):
    serializer=TeamAddSerializer(data=request.data)
    permission_classes = [permissions.IsAdminUser]
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
