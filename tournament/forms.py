from .models import Team,Match,TeamMatch
from django.forms import forms

class TeamForm(forms.Form):
    class Meta:
        model = Team
        fields = "__all__"