from django.db import models

# Create your models here.

class Team(models.Model):
    country = models.CharField(max_length=3, unique=True)

class Match(models.Model):
    home_team = models.ForeignKey(Team,on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team,on_delete=models.CASCADE)
    date = models.DateField()

