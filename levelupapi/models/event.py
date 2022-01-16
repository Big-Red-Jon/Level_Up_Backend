from django.db import models
# from django.contrib.auth.models import User
from levelupapi.models.gamer import Gamer
from levelupapi.models.game import Game


class Event(models.Model):

    organizer = models.ForeignKey(Gamer, on_delete=models.CASCADE, default='')
    description = models.CharField(max_length=55, default='Game_Night')
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date = models.DateField((""), auto_now=False,
                            auto_now_add=False, default='None')
    time = models.TimeField((u"Conversation Time"),
                            blank=True, default='Some Time')
    attendees = models.ManyToManyField(
        'levelupapi.gamer', related_name='attending')

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value
