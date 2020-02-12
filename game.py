from tictactoe import Tictactoe


def main():
    x = 0
    game = Tictactoe()
    while True:
        for i in [1, 4, 7]:
            print(game.myfunc(i))
        while True:
            choice = input(
                "Player {} Enter your move(1-9):".format(x+1)).strip()
            try:
                choice = int(choice)
            except:
                print("Invalid Number!")
                choice = -1
            if 1 <= choice <= 9:
                break
            else:
                print ('Please enter valid input between 1 - 9')
        if game.board[choice - 1] == ' ':
            if x == 0:
                game.board[choice - 1] = 'X'
                if game.isVictory('X'):
                    print('\n Player {} is the winner!'.format(x+1))
                    break
                x = 1
            else:
                game.board[choice - 1] = 'Y'
                if game.isVictory('Y'):
                    print('\n Player {} is the winner!'.format(x+1))
                    break
                x = 0
        else:
            print("\n Space is taken!")


if __name__ == "__main__":
    main()