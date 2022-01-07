# Used for type checking
from typing import Tuple
# The connect4 logic class
from Connect4Logic import Connect4
# The TicTacToe logic class
from TicTacToeLogic import TicTacToe
# The MinMaxLogic class
from MinMaxLogic import MinMaxAI
# Gets a random number in a range
from random import randint


class Run_Game:
    def __init__(self, game: Tuple[TicTacToe, Connect4] = None, start: bool = False) -> None:
        """
            Class to start the game with the AI and controls the logic of the game

        Args:
            game (Tuple[TicTacToe, Connect4], optional): The game object. Defaults to create a game object.
            start (bool, optional): flag for if you want the AI to start. Defaults to False.
        """
        if game:
            self.__game = game
        else:
            self.__game = TicTacToe()
        self.game_board = self.__game.tic_board
        self.ai = MinMaxAI(self.__game, True)
        if start:
            x_rand = randint(0, 2)
            y_rand = randint(0, 2)
            self.run(x_rand, y_rand)

    def run(self, x: int = None, y: int = None, do_nothing: bool = False) -> bool:
        """
            Function to play one move if nothing is passed then the AI will play

        Args:
            x (int, optional): x corrds to play. Defaults to None.
            y (int, optional): y corrds to play. Defaults to None.
            do_nothing (bool, optional): The AI doesn't play. Defaults to False.

        Returns:
            bool: if the move was played correctly or not
        """
        if self.isWin():
            return False
        if self.__game.turn:
            x_ai, y_ai = self.ai.best_move("X")
        else:
            x_ai, y_ai = self.ai.best_move("O")
        print("--------------------------------")
        if x is not None:
            return self.__game.play(x, y)
        if not do_nothing:
            return self.__game.play(x_ai, y_ai)

    def isWin(self) -> bool:
        """
            Fuction to know if the game has ended or not

        Returns:
            bool: True if the game has ended else False
        """
        if self.__game.win() != "":
            return True
        else:
            return False

    def movesLeft(self) -> int:
        """
            Fuction to know the number of moves left in the game

        Returns:
            int: The number of moves left
        """
        return self.__game.movesLeft()
