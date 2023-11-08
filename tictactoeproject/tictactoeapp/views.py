from django.shortcuts import render
from django.http import JsonResponse
from .models import Game

def game_board(request):
    game = Game.objects.first()  # Retrieve the game instance (assuming there's only one game)
    return render(request, 'tictactoeapp/game_board.html', {'game': game})

def make_move(request):
    if request.method == 'POST':
        cell_id = request.POST.get('cellId')  # Get the cell ID from the POST data

        # Assuming you have a Game model with attributes like 'board', 'current_player', 'winner', etc.
        game = Game.objects.first()  # Retrieve the game instance (assuming there's only one game)

        # Check if the selected cell is empty and the game is not over
        if game.board[int(cell_id)] == ' ' and not game.winner:
            # Update the board with the current player's symbol ('X' or 'O')
            game.board = game.board[:int(cell_id)] + game.current_player + game.board[int(cell_id) + 1:]

            # Check for a win or a draw
            if check_winner(game.board):
                game.winner = game.current_player
            elif ' ' not in game.board:  # Check for a draw
                game.winner = 'Draw'
            
            # Toggle the current player
            game.current_player = 'X' if game.current_player == 'O' else 'O'

            # Save the updated game state
            game.save()

            # Return a JSON response with the updated game state and winner
            return JsonResponse({'message': 'Move successful', 'game_state': 'updated_game_state', 'winner': game.winner})

    # Handle other HTTP methods as needed
    return JsonResponse({'message': 'Invalid request'})


def check_winner(board):
    # Define winning combinations
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for combo in winning_combinations:
        a, b, c = combo
        if board[a] == board[b] == board[c] != ' ':
            return True

    return False
