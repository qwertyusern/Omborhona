from django.urls import path
from .views import *
urlpatterns = [
    path('mahsulot/', MahsulotView.as_view(), name="mahsulot"),
    path('client/', ClientView.as_view(), name="client"),
    path('bolim/', BolimView.as_view(), name="bolim"),
]