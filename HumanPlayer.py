from Player import Player


class HumanPlayer(Player):

    def __init__(self, id):
        super().__init__(id)

    def getAction(self, board):
        while True:
            player_input = input(f"Player {self.id}, enter row, column: ")
            player_input = tuple(map(int, player_input.split(",")))

            if board[player_input] == 0:
                return player_input
            else:
                print("Please enter valid move!")