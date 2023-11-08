from django.urls import path
from . import views

urlpatterns = [
    path('board/', views.game_board, name='game_board'),
]
