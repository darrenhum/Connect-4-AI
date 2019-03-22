import copy
import random
import math

class Minimax:

    def __init__(self, board):
        self.board = copy.deepcopy(board)
        self.pieces = ["O", "X"]
        self.iter = 0

    def terminal_node(self, player):
        # If there are no moves for this player, game is over
        if (not self.board.get_add_moves() and not self.board.get_remove_moves(player)) or \
            self.check_for_streak(self.board, self.pieces[0], 4) > 4 or \
            self.check_for_streak(self.board, self.pieces[1], 4) > 4:
            return True
        return False

    def generate_boards(self, board, currentPlayer):
        result = []

        # TODO
        addcounter = 0

        for addMove in board.get_add_moves():
            tempBoard = copy.deepcopy(board)
            tempBoard.add_piece(addMove, currentPlayer)
            result.append(tempBoard)
            addcounter += 1

        return result

    def bestMove(self, board, depth, currentPlayer):
        boards = self.generate_boards(board, currentPlayer)
        moves = []

        for new_board in boards:
            moves.append(tuple([new_board, self.minimax(\
                new_board, \
                depth-1, \
                -999999, \
                999999, \
                self.opposite_player(currentPlayer))]))

        best_alpha = -99999999
        best_move = None

        random.shuffle(moves)
        for move, alpha in moves:
            #print("Position:", move.pos, "Alpha:", alpha)

            if alpha >= best_alpha:
                best_alpha = alpha
                best_move = move

        #print(self.iter, " nodes visited")
        return best_move, best_alpha

    def minimax(self, inboard, depth, alpha, beta, currentPlayer):
        board = copy.deepcopy(inboard)
        
        if depth == 0 or self.terminal_node(currentPlayer):
            self.iter += 1
            return self.heuristic2(board, currentPlayer)

        moves = self.generate_boards(board, currentPlayer)

        if currentPlayer == self.pieces[1]:
            value = -999999
            for child in moves:
                value = max(value, self.minimax(child, depth - 1, alpha, beta, self.opposite_player(currentPlayer)))
                alpha = max(alpha, value)
                if alpha >= beta:
                    break # (* beta cut-off *)
            return value

        else:
            value = 999999
            for child in moves:
                value = min(value, self.minimax(child, depth - 1, alpha, beta, self.opposite_player(currentPlayer)))
                beta = min(beta, value)
                if alpha >= beta:
                    break #(* alpha cut-off *)
            return value
        
    # Heuristic 1
    # Give weight to each streak
    # Sum weights
    def heuristic(self, board, player):
        value = 10000 * self.check_for_streak(board, player, 4) + \
            100 * self.check_for_streak(board, player, 3) + \
            10 * self.check_for_streak(board, player, 2)
        
        opponent = self.check_for_streak(board, self.opposite_player(player), 4)
        
        if opponent > 0:
            value = -20000

        return value
        
    # Heuristic 2
    # Same as 1, but subtract opponents
    def heuristic2(self, board, player):
        return round(1.3 * self.heuristic(board, player), 4) - round(1.2 * self.heuristic(board, self.opposite_player(player)), 4)

    def check_for_streak(self, board, piece, streak):
        count = 0
        # For each piece in the board
        for i in range(board.rows):
            for j in range(board.cols):
                if board.board[i][j].lower() == piece.lower():
                    # Check if a vertical streak starts at (i, j)
                    count += self.vertical_streak(i, j, board, streak)
                    
                    # Check if a horizontal four-in-a-row starts at (i, j)
                    count += self.horizontal_streak(i, j, board, streak)
                    
                    # Check if a diagonal (either way) four-in-a-row starts at (i, j)
                    count += self.diagonal_check(i, j, board, streak)
        # Return the sum of streaks of length 'streak'
        return count
            
    def vertical_streak(self, row, col, board, streak):
        consecutiveCount = 0
        for i in range(row, board.rows):
            if board.board[i][col].lower() == board.board[row][col].lower():
                consecutiveCount += 1
            else:
                break
    
        if consecutiveCount >= streak:
            return 1
        else:
            return 0
    
    def horizontal_streak(self, row, col, board, streak):
        consecutiveCount = 0
        for j in range(col, board.cols):
            if board.board[row][j].lower() == board.board[row][col].lower():
                consecutiveCount += 1
            else:
                break

        if consecutiveCount >= streak:
            return 1
        else:
            return 0
    
    def diagonal_check(self, row, col, board, streak):

        total = 0
        # Check for diagonals with positive slope
        consecutiveCount = 0
        j = col
        for i in range(row, board.rows):
            if j > board.rows:
                break
            elif board.board[i][j].lower() == board.board[row][col].lower():
                consecutiveCount += 1
            else:
                break
            j += 1 # Increment column when row is incremented
            
        if consecutiveCount >= streak:
            total += 1

        # Check for diagonals with negative slope
        consecutiveCount = 0
        j = col
        for i in range(row, -1, -1):
            if j > board.rows:
                break
            elif board.board[i][j].lower() == board.board[row][col].lower():
                consecutiveCount += 1
            else:
                break
            j += 1 # Increment column when row is incremented

        if consecutiveCount >= streak:
            total += 1

        return total

    def opposite_player(self, player):
        if player == self.pieces[0]:
            return self.pieces[1]
        else:
            return self.pieces[0]