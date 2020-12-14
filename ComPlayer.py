import numpy as np
from Player import Player
from util import moveList, flipBoard, getBoardIndex, getValidMoves


class ComPlayer(Player):

    def __init__(self, id, q_table):
        super().__init__(id)
        self.q_table = q_table

    def getAction(self, board):
        if self.id == 2:
            new_board = flipBoard(board)
        else:
            new_board = board

        validMoves = getValidMoves(new_board)
        validIndices = []

        for move in validMoves:
            validIndices.append(moveList.index(move))

        boardIndex = getBoardIndex(new_board)

        valid_moves_with_q_values = self.q_table[boardIndex][validIndices]

        index = int(np.argmax(valid_moves_with_q_values))

        return validMoves[index]
