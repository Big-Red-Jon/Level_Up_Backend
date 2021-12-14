from django.db import models
from django.contrib.auth.models import User


class Events(models.Model):
    eventTitle = models.CharField(max_length=55)
    date = models.DateField((""), auto_now=False, auto_now_add=False)
    # Ask about this
    userId = models.OneToOneField(User, on_delete=models.CASCADE)


#      id integer
#   eventTitle varchar
#   date varchar
#   userId integer
#   gameId integer
