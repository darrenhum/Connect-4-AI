from ai import Ai
from player import Player
from board import Board

class Game:
    currentTurn = None
    players = []
    gameMode = None

    def __init__(self, rows=None, cols=None):
        self.rows = rows or 6
        self.cols = cols or 7
        self.board = Board(self.rows, self.cols)

        player = input("Player 1 human or cpu?(h/c)")
        if player == 'h':
            self.players.append(Player("O"))
        else:
            self.players.append(Ai("O", 4))

        player = input("Player 2 human or cpu?(h/c)")
        if player == 'h':
            self.players.append(Player("X"))
        else:
            self.players.append(Ai("X", 4))

        self.currentTurn = self.players[0]

    def __str__(self):
        result = ''
        for row in range(self.rows):
            for col in range(self.cols):
                result += self.board.board[row][col] + " "
            result += '\n'
        result += "0 1 2 3 4 5 6"
        return result
    
    def next_move(self):
        print()
        print(self.board)
        print(self.currentTurn.piece + "'s turn.")
        player = self.currentTurn

        self.board = player.move(self.board)
        print(self.board.move)

        self.change_player()

        return self.board.check_win(self.players[0].piece) or \
                self.board.check_win(self.players[1].piece)

    def change_player(self):
        if self.currentTurn == self.players[0]:
            self.currentTurn = self.players[1]
        else:
            self.currentTurn = self.players[0]
