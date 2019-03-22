class Player:

    def __init__(self, piece):
        self.piece = piece

    def move(self, board):
        valid = False
        while not valid:

            try:
                position = input("Enter column to play: ")
                if int(position) >= board.cols:
                    raise ValueError

                moves = board.get_add_moves()
                if int(position) not in moves:
                    raise ValueError
                else:
                    valid = True
            except KeyboardInterrupt:
                break
            except:
                print("Invalid selection.")
                continue
            
        board.add_piece(int(position), self.piece)
        return board