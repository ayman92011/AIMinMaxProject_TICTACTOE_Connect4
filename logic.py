from TicTacToeLogic import TicTacToe
from MinMaxLogic import MinMaxAI


if __name__ == "__main__":
    game = TicTacToe()
    ai_x = MinMaxAI("X", game)
    ai_o = MinMaxAI("O", game)
    while game.win() == "":

        x, y = ai_x.findBestMove()
        game.play(x, y)
        print(game)
        if game.win() == "":
            x, y = ai_o.findBestMove()
            game.play(x, y)
            print(game)
        else:
            break

    print(game.win())
