class Board:

    def __init__(self, rows=None, cols=None):
        self.rows = rows or 6
        self.cols = cols or 7
        self.board = [["." for x in range(self.cols)] for x in range(self.rows)]
        self.colCounter = [0] * self.cols
        self.move = None
        self.pos = None

    def __str__(self):
        result = ''
        for row in range(self.rows):
            for col in range(self.cols):
                result += self.board[row][col] + " "
            result += '\n'
        result += "0 1 2 3 4 5 6"
        return result

    def add_piece(self, col, player):
        self.board[self.rows - self.colCounter[col] - 1][col] = player
        self.colCounter[col] += 1
        self.move = player + " added at " + str(col)
        self.pos = col
    
    def check_win(self, player):
        # Horizontal check
        for j in range(self.cols-3):
            for i in range(self.rows):
                if self.board[i][j] == player and \
                        self.board[i][j+1] == player and \
                        self.board[i][j+2] == player and \
                        self.board[i][j+3] == player:
                    return True

        # Vertical check
        for i in range(self.rows-3):
            for j in range(self.cols):
                if self.board[i][j] == player and \
                        self.board[i+1][j] == player and \
                        self.board[i+2][j] == player and \
                        self.board[i+3][j] == player:
                    return True
        
        # Ascending diagonal check
        for i in range(3, self.rows):
            for j in range(self.cols-3):
                if self.board[i][j] == player and \
                        self.board[i-1][j+1] == player and \
                        self.board[i-2][j+2] == player and \
                        self.board[i-3][j+3] == player:
                    return True

        # Descending diagonal check
        for i in range(3, self.rows):
            for j in range(3, self.cols):
                if self.board[i][j] == player and \
                        self.board[i-1][j-1] == player and \
                        self.board[i-2][j-2] == player and \
                        self.board[i-3][j-3] == player:
                    return True
        return False

    # Returns a list of all columns that are not full
    def get_add_moves(self):
        result = []
        for x in range(len(self.colCounter)):
            if self.colCounter[x] < self.rows:
                result.append(x)
        return result