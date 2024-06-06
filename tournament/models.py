from django.db import models

# Create your models here.

class Team(models.Model):
    country = models.CharField(max_length=3, unique=True)

    def matches_played(self):
        matches = TeamMatch.objects.filter(team_id=self.id).count()
        return matches
    
    def matches_won(self):
        wins = Match.objects.filter(winning_team_id=self.id).count()
        return wins 
    
    def matches_lost(self):
        losses = TeamMatch.objects.filter(team_id=self.id).count() - Match.objects.filter(winning_team_id=self.id).count()
        return losses

class Match(models.Model):
    home_team = models.ForeignKey(Team,on_delete=models.CASCADE,related_name="home_team")
    away_team = models.ForeignKey(Team,on_delete=models.CASCADE,related_name="away_team")
    date = models.DateField()
    winning_team = models.ForeignKey(Team,on_delete=models.CASCADE,related_name="winner_team",default=home_team)


class TeamMatch(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_matches')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='team_matches')
    batting_score = models.IntegerField()
    batting_wickets = models.IntegerField()
    batting_overs = models.IntegerField()


