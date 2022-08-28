from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:tournament_id>', views.about_tournament, name='tournament'),
]

