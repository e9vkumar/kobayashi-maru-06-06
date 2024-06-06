from django.urls import path
from .views import TeamListView,TeamDetail,TeamForm

urlpatterns = [
    path('', TeamListView.as_view(),name="team_list"),
    path('<int:pk>/', TeamDetail.as_view(),name="team_detail"),
    path('teamform/',TeamForm.as_view(),name="team-form"),
]