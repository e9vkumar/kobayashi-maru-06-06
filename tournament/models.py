from django.db import models

# Create your models here.

class Team(models.Model):
    country = models.CharField(max_length=3, unique=True)

