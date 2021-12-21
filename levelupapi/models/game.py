from django.db import models

from levelupapi.models.gamer import Gamer
from levelupapi.models.gametype import GameType
# from django.contrib.auth.models import Game


class Game(models.Model):

    title = models.CharField(max_length=55)
    maker = models.CharField(max_length=55, default='Some Creator')
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    game_type = models.ForeignKey(GameType, on_delete=models.CASCADE)
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()


# related name (optional)
# to and on delete
# related model
