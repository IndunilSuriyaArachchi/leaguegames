from rest_framework import serializers
from . models import *

class PlayerSerializer(serializers.ModelSerializer):
    team = serializers.CharField(source="team.team_name", read_only=True)
    class Meta:
        model = Player
        fields = ['id', 'team','fname','lname','height_cm','avg_score', 'played_games','percentile' ]	
        
    percentile = serializers.SerializerMethodField(method_name='calculate_percentile')
    def calculate_percentile(self, player:Player):
        return player.avg_score*player.played_games
    #SELECT * FROM "game_player" where team_id=1 and avg_score>= (SELECT (sum(avg_score)*.9)/count(id) FROM "game_player" where team_id=1);

class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ['id', 'fname','lname']

class TeamSerializer(serializers.ModelSerializer):
    coach=CoachSerializer()
    player_set=PlayerSerializer(many=True)
    class Meta:
        model = Team
        #fields = '__all__'
        fields = ['id', 'team_name','total_score','played_games','team_avg', 'coach', 'player_set']

class TeamAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        #fields = '__all__'
        fields = ['id', 'team_name','total_score','played_games','team_avg']

class TeamSerializerWithoutAllPlayers(serializers.ModelSerializer):
    coach=CoachSerializer()
    class Meta:
        model = Team
        #fields = '__all__'
        fields = ['id', 'team_name','total_score','played_games','team_avg', 'coach', ]


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class GamePlayTeamSerializer(serializers.ModelSerializer):
    team=TeamSerializerWithoutAllPlayers()
    player=PlayerSerializer()
    class Meta:
        model = GamePlayTeam
        #fields = '__all__'
        fields = ['team','player', 'score']

class GameTeamSerialier(serializers.ModelSerializer):
    game=GameSerializer()
    team=TeamSerializerWithoutAllPlayers()
    class Meta:
        model = GameTeam
        fields = ['game', 'team','status','team_score']

