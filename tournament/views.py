from django.shortcuts import render
from django.views import generic
from .models import Team,Match,TeamMatch
from .forms import TeamForm

# Create your views here.

class TeamListView(generic.ListView):
    template_name = "team_list.html"
    model = Team
    context_object_name = "teams"


class TeamDetail(generic.DetailView):
    template_name = "team_detail.html"
    model = Team
    context_object_name="team"


class TeamForm(generic.FormView):
    template_name = "team_form.html"
    form = TeamForm
