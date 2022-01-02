from TicTacToeLogic import TicTacToe
from MinMaxLogic import MinMaxAI


class Run_Game:
    def __init__(self, game=None, start=False) -> None:
        if game:
            self.game = game
        else:
            self.game = TicTacToe()

        self.start = start
        self.ai_x = MinMaxAI("X", self.game)
        self.ai_o = MinMaxAI("O", self.game)

    def run(self, x=None, y=None):
        if self.isWin():
            return 0
        if self.start:
            self.start = False
            return self.game.play(self.ai_x.findBestMove())
        if x is not None:
            return self.game.play(x, y)

        if self.game.turn:
            x, y = self.ai_x.findBestMove()
        else:
            x, y = self.ai_o.findBestMove()
        return self.game.play(x, y)

    def isWin(self):
        if self.game.win() != "":
            return True
        else:
            return False
