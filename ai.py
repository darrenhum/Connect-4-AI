from minimax import Minimax
import time
import random

class Ai:
    def __init__(self, piece, depth=None):
        self.piece = piece
        self.depth = depth or 4

    def move(self, board):
        time.sleep(1)
        minimax = Minimax(board)
        x = minimax.bestMove(board, self.depth, self.piece)
        return x[0]
