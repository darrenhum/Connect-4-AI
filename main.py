from game import Game

def main():
    p1 = 0
    p2 = 0
    again = 'y'
    while(again == 'y'):
        game = Game()

        won = False
        while not won:
            won = game.next_move()
        print(game.board)

        if game.board.check_win(game.players[0].piece):
            print("Player " + game.players[0].piece + " won!")
            p1 += 1
        else:
            print("Player " + game.players[1].piece + " won!")
            p2 += 2

        again = input("Would you like to play again? (y/n)")

    print("Scores: Player 1 - " + str(p1))
    print("        Player 2 - " + str(p2))

if __name__== "__main__":
    main()