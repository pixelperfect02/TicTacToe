from django.db import models

class Game(models.Model):
    board = models.CharField(max_length=9, default=' ' * 9)
    next_move = models.CharField(max_length=1, default='X')

    class Meta:
        app_label = 'tictactoeapp'
