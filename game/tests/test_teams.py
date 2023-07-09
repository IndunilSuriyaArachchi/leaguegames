from rest_framework.test import APIClient
from rest_framework import status
import pytest

@pytest.mark.django_db
class TestGetTeams:
    def test_team_api_when_user_not_athenticated(self):
        client = APIClient()
        response=client.get('/leaguegames/team/')

        assert response.status_code ==status.HTTP_401_UNAUTHORIZED

    def test_game_api_when_user_not_athenticated(self):
        client = APIClient()
        response=client.get('/leaguegames/game/')

        assert response.status_code ==status.HTTP_401_UNAUTHORIZED

    def test_player_api_when_user_not_athenticated(self):
        client = APIClient()
        response=client.get('/leaguegames/player/')

        assert response.status_code ==status.HTTP_401_UNAUTHORIZED

    def test_player_detail_api_when_user_not_athenticated(self):
        client = APIClient()
        response=client.get('/leaguegames/player/1/')

        assert response.status_code ==status.HTTP_401_UNAUTHORIZED

