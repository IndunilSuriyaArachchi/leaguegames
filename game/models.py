from django.db import models
from django.conf import settings

class Game(models.Model):

    GAME_STATUS=[
        ('P', 'Pendig'),
        ('S', 'Started'),
        ('F', 'Finished'),
    ]
    GAME_LEVEL=[
        ('L1', 'Level1'),
        ('L2', 'Level2'),
	    ('SF', 'SemiFinal'),
        ('F', 'Final'),
    ]

    game_id=models.IntegerField(primary_key=True,auto_created=True)
    game_level=models.CharField(max_length=2, choices=GAME_LEVEL, default='L1')
    game_date=models.DateField()
    venue=models.CharField(max_length=255)
    status=models.CharField(max_length=1, choices=GAME_STATUS, default='P')

class Team(models.Model):
	id=models.IntegerField(primary_key=True, auto_created=True)
	team_name=models.CharField(max_length=255)
	total_score=models.IntegerField()
	played_games=models.IntegerField()
	team_avg=models.DecimalField(max_digits=4, decimal_places=2)
		
class Player(models.Model):
	id=models.IntegerField(primary_key=True)
	#fname=models.CharField(max_length=255)
	#lname=models.CharField(max_length=255)
	height_cm=models.IntegerField()
	avg_score=models.DecimalField(max_digits=4, decimal_places=2)
	played_games=models.IntegerField()
	team=models.ForeignKey(Team, on_delete=models.CASCADE)
	user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.fname} {self.lname}'

class GameTeam(models.Model):
	GAME_TEAM_STATUS=[
		('P', 'Pendig'),
        ('W', 'Win'),
        ('L', 'LOOS'),
        ('D', 'Draw'),
    ]
	
	game=models.ForeignKey(Game,on_delete=models.CASCADE)
	team=models.ForeignKey(Team, on_delete=models.CASCADE)
	status=models.CharField(max_length=1, choices=GAME_TEAM_STATUS, default='P')
	team_score=models.IntegerField()

class GamePlayTeam(models.Model):

	game=models.ForeignKey(Game, on_delete=models.CASCADE)
	team=models.ForeignKey(Team, on_delete=models.CASCADE)
	player=models.ForeignKey(Player, on_delete=models.CASCADE)
	score=models.IntegerField()
	class Meta:
		unique_together = (('game','team','player'),)
	
class Coach(models.Model):
	id=models.IntegerField(primary_key=True)
	#fname=models.CharField(max_length=255)
	#lname=models.CharField(max_length=255)
	team=models.OneToOneField(Team, on_delete=models.CASCADE)
	user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

#class LeagueAdmin(models.Model):
#	id=models.IntegerField(primary_key=True)
#	fname=models.CharField(max_length=255)
#	lname=models.CharField(max_length=255)