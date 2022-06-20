from django.urls import path
from .views import *
urlpatterns = [
     path('statistika/', StatsView.as_view(), name="stats"),
]