import numpy as np

moveList = []

for i in range(3):
    for j in range(3):
        moveList.append((i, j))


def getWinner(board):

    # Check each column
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            if board[i][0] != 0:
                return int(board[i][0])

    # Check each row
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[0][i] != 0:
                return int(board[0][i])

    # Check diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] != 0:
            return int(board[0][0])

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] != 0:
            return int(board[0][2])

    return None


def checkStalemate(board):
    return np.all(board)


def getBoardIndex(board):
    result = ""
    for i in range(3):
        for j in range(3):
            result += str(int(board[i, j]))

    return int(result, 3)


def flipBoard(board):
    new_board = np.zeros((3, 3))

    for i in range(3):
        for j in range(3):
            if board[i, j] == 1:
                new_board[i, j] = 2
            elif board[i, j] == 2:
                new_board[i, j] = 1

    return new_board


def getValidMoves(board):
    moves = []

    for i in range(3):
        for j in range(3):
            if board[i, j] == 0:
                moves.append((i, j))

    return moves


def getBoardCopy(board):
    new_board = np.zeros((3, 3))

    for i in range(3):
        for j in range(3):
            new_board[i, j] = board[i, j]

    return new_board
