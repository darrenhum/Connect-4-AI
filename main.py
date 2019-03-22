from game import Game

def main():
    game = Game()

    won = False
    while not won:
        won = game.next_move()
    print(game.board)

    if game.board.check_win(game.players[0].piece):
        print("Player " + game.players[0].piece + " won!")
    else:
        print("Player " + game.players[1].piece + " won!")

if __name__== "__main__":
    main()