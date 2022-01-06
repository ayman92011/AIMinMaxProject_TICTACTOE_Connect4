from TicTacToeLogic import TicTacToe
from MinMaxLogic import MinMaxAI


class Run_Game:
    def __init__(self, game=None, start=False) -> None:
        if game:
            self.game = game
        else:
            self.game = TicTacToe()

        self.start = start
        self.ai = MinMaxAI(self.game, True)

    def run(self, x=None, y=None, do_nothing=False):
        if self.isWin():
            return 0
        if self.game.turn:
            x_ai, y_ai = self.ai.best_move("X")
        else:
            x_ai, y_ai = self.ai.best_move("O")
        print("--------------------------------")
        if self.start:
            self.start = False
            return self.game.play(x_ai, y_ai)
        if x is not None:
            return self.game.play(x, y)
        if not do_nothing:
            return self.game.play(x_ai, y_ai)

    def isWin(self):
        if self.game.win() != "":
            return True
        else:
            return False
