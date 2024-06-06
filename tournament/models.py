from django.db import models

# Create your models here.

class Team(models.Model):
    country = models.CharField(max_length=3, unique=True)

    def matches_played(self):
        matches = TeamMatch.objects.filter(team_id=self.id).count()

class Match(models.Model):
    home_team = models.ForeignKey(Team,on_delete=models.CASCADE,related_name="home_team")
    away_team = models.ForeignKey(Team,on_delete=models.CASCADE,related_name="away_team")
    date = models.DateField()


class TeamMatch(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_matches')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='team_matches')
    batting_score = models.IntegerField()
    batting_wickets = models.IntegerField()
    batting_overs = models.IntegerField()


