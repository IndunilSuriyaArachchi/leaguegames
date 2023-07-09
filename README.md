# leaguegames
Python Assesment for metafic.

# Created API/Views

- View all teams with coach, excluding players [ADMIN]
http://127.0.0.1:8000/leaguegames/team/

- View Specific team including players [ADMIN,COACH]
http://127.0.0.1:8000/leaguegames/team/2/

- Add/create a team (Optional, to test selectplayers/ API) [ADMIN,COACH]
http://127.0.0.1:8000/leaguegames/team/add/

- View all players [ADMIN]
http://127.0.0.1:8000/leaguegames/player/

- view Specific player details [ADMIN,COACH,PLAYER]
http://127.0.0.1:8000/leaguegames/player/1/

- View all games (excluding teams) [ADMIN,COACH,PLAYER]
http://127.0.0.1:8000/leaguegames/game/

- View Specific game including team [ADMIN,COACH]
http://127.0.0.1:8000/leaguegames/game/1/

- View Specific game playing team [ADMIN,COACH]
http://127.0.0.1:8000/leaguegames/game/1/player/

- Add Players to specific game [ADMIN,COACH]
http://127.0.0.1:8000/leaguegames/game/selectplayers/

- to get jwt access token
http://127.0.0.1:8000/auth/jwt/create
- after expired, to get new access token, we must send refresh to token to following
http://127.0.0.1:8000/auth/jwt/refresh

# Implementation
***
- Followed "The Ultimate Django Series", all three series by Mosh Hamedani, as a study guide
- Apps details
- [Leaguegames] - The main app
- [Game] - Game/matches manage and to display scoreboard
- [Team] - created for team player data manage, but not used, team also managed at Game app
- [Core] - user data manage
- Used djoser for JWT authentication, and pytest for testing
- Generated mock data with "mackaroo"
- Test user details : username = user1 / password = ILoveDjango
# Pending work
***
- selectplayers/ API could not be tested, as gray areas in composite keys [game, team, player] saving part knowledge
- As per my knowledge, 90th percentile players can be get by query like below (note: this is not optimized, just to test )
> SELECT * FROM "game_player" where team_id=1 and avg_score>= (SELECT (sum(avg_score)*.9)/count(id) FROM "game_player" where team_id=1);

But as I'm not aware how to handle queries at django serialiers, I could not able to do that part.
- Pytest testing only done for few senarios in one API 
- User statistics part has not implemented

# Used python version 3.11.4
