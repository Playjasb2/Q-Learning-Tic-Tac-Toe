from HumanPlayer import HumanPlayer
from ComPlayer import ComPlayer
from util import *

board = np.zeros((3, 3), dtype=int)

# load q_table npy file here
q_table = np.load("")

Player1 = HumanPlayer(1)
Player2 = ComPlayer(2, q_table)

currentPlayer = Player1

while True:
    player_input = currentPlayer.getAction(board)

    board[player_input] = currentPlayer.id

    print(board)

    winner = getWinner(board)

    if winner:
        print(f"Player {winner} win!")
        break

    if checkStalemate(board):
        print("Draw!")
        break

    if currentPlayer == Player1:
        currentPlayer = Player2
    else:
        currentPlayer = Player1

