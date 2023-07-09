# leaguegames
Python Assesment for metafic.

# Created API/Views

- View all teams with coach, excluding players [ADMIN]
/leaguegames/team/

- View Specific team including players [ADMIN,COACH]
/leaguegames/team/2/

- Add/create a team (Optional, to test selectplayers/ API) [ADMIN,COACH]
/leaguegames/team/add/

- View all players [ADMIN]
/leaguegames/player/

- view Specific player details [ADMIN,COACH,PLAYER]
/leaguegames/player/1/

- View all games (excluding teams) [ADMIN,COACH,PLAYER]
/leaguegames/game/

- View Specific game including team [ADMIN,COACH]
/leaguegames/game/1/

- View Specific game playing team [ADMIN,COACH]
/leaguegames/game/1/player/

- Add Players to specific game [ADMIN,COACH]
/leaguegames/game/selectplayers/

- to get jwt access token
/auth/jwt/create
- after expired, to get new access token, we must send refresh to token to following
/auth/jwt/refresh

# Implementation
***
- Followed "The Ultimate Django Series", all three series by Mosh Hamedani, as a study guide
- Used djoser for JWT authentication, and pytest for testing
- Generated mock data with "mackaroo"
# Pending work
***
- selectplayers/ API could not be tested, as gray areas in composite keys [game, team, player] saving part knowledge
- As per my knowledge, 90th percentile players can be get by query like below (note: this is not optimized, just to test )
> SELECT * FROM "game_player" where team_id=1 and avg_score>= (SELECT (sum(avg_score)*.9)/count(id) FROM "game_player" where team_id=1);

But as I'm not aware how to handle queries at django serialiers, I could not able to do that part.
- Pytest testing only done for few senarios in one API 
- User statistics part has not implemented

# Used python version 3.11.4
