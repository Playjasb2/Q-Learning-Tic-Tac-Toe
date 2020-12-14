from ComPlayer import ComPlayer
from util import *
from tqdm import tqdm
import time

EPISODES = 50000
LEARNING_RATE = 0.1
DISCOUNT = 0.95

epsilon = 0.5
ep_decay = 0.5/EPISODES

q_table = np.random.uniform(-2, 0, (3**9, 9))

board = np.zeros((3, 3), dtype=int)

Player1 = ComPlayer(1, q_table)
Player2 = ComPlayer(2, q_table)

last_board = None
last_action = None

for episode in tqdm(range(EPISODES)):
    board = np.zeros((3, 3), dtype=int)
    current_player = Player1
    while True:
        if current_player == Player2:
            new_board = flipBoard(board)
        else:
            new_board = board

        if np.random.random() > epsilon:
            action = current_player.getAction(board)
        else:
            validMoves = getValidMoves(new_board)
            index = np.random.randint(0, len(validMoves))
            action = validMoves[index]

        current_q = q_table[(getBoardIndex(new_board),) + (moveList.index(action),)]

        board[action] = current_player.id

        winner = getWinner(board)

        if winner:
            if winner == 1:
                q_table[(getBoardIndex(board),) + (moveList.index(action),)] = 10
                new_board = flipBoard(last_board)
                q_table[(getBoardIndex(new_board),) + (moveList.index(last_action),)] = -10
            else:
                new_board = flipBoard(board)
                q_table[(getBoardIndex(new_board),) + (moveList.index(action),)] = 10
                q_table[(getBoardIndex(last_board),) + (moveList.index(last_action),)] = -10

            break

        if checkStalemate(board):
            if current_player == Player1:
                q_table[(getBoardIndex(board),) + (moveList.index(action),)] = 0
                new_board = flipBoard(last_board)
                q_table[(getBoardIndex(new_board),) + (moveList.index(last_action),)] = 0
            else:
                new_board = flipBoard(board)
                q_table[(getBoardIndex(new_board),) + (moveList.index(action),)] = 0
                q_table[(getBoardIndex(last_board),) + (moveList.index(last_action),)] = 0

            break

        max_future_q = np.max(q_table[getBoardIndex(new_board)])

        reward = -1

        new_q = current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q - current_q)
        q_table[(getBoardIndex(new_board),) + (moveList.index(action),)] = new_q

        last_action = action
        last_board = getBoardCopy(board)

        Player1.q_table = q_table
        Player2.q_table = q_table

        epsilon -= ep_decay

        if epsilon < 0:
            epsilon = 0

        if current_player == Player1:
            current_player = Player2
        else:
            current_player = Player1

np.save(f"q_table-{int(time.time())}.npy", q_table)



