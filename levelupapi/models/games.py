from django.db import models
# from django.contrib.auth.models import Game


class Games(models.Model):

    name = models.CharField(max_length=55)
    type = models.CharField(max_length=55)
    genre = models.CharField(max_length=55)
    ageRange = models.CharField(max_length=12)

#   id integer
#   name varchar
#   type varchar
#   genre varchar
#   ageRange varchar
