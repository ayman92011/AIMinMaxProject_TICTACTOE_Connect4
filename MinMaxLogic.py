# To know how much time pass in each search for the best move
import time
# For Type checking
from typing import Tuple, Union
# The Connect4 Logic class
from Connect4Logic import Connect4
# The TicTacToe Logic class
from TicTacToeLogic import TicTacToe
import functools
var = 100000


class MinMaxAI:
    def __init__(self, game: Union[TicTacToe, Connect4] = None, alphabeta: bool = False) -> None:
        """
            Class for the logic of the MinMax AI made with MinMax and AlphaBeta.

        Args:
            game (Union[TicTacToe, Connect4], optional): The game object can be TicTacToe or Connect4. Defaults to None.
            alphabeta (bool, optional): Flag for when you want to use alpha beta. Defaults to False.
        """
        if game == None:
            game = TicTacToe()
        else:
            self.game = game
        if isinstance(self.game, TicTacToe):
            self.game_board = self.game.tic_board
            self.row = self.col = 3
        else:
            self.game_board = self.game.connect_board
            self.row = 6
            self.col = 7
        self.alphabeta = alphabeta

    def is_valid(self, px: int, py: int) -> bool:
        """
            Checks if you want to play a valid move or not

        Args:
            px (int): The x corrds for the move
            py (int): The y corrds for the move

        Returns:
            Bool: true if the move is valid else returns false
        """
        if px < 0 or px > self.row-1 or py < 0 or py > self.col - 1:
            return False
        elif self.game_board[px][py] != ' ':
            return False
        else:
            return True

    def is_end(self) -> str:
        """
            Checks if any player wins or there is no other moves to play

        Returns:
            str: X if x wins, Y if y wins, . if it is a draw, None if the game hasm't ended
        """
        if self.game.win() == "X wins":
            return "X"
        elif self.game.win() == "O wins":
            return "O"
        elif self.game.win() == "Draw":
            return "."

        return None

    @functools.lru_cache(var)
    def max(self) -> Tuple[int, int, int]:
        """
            Function for the max value calls min recersevly to detrmine the best move for the O player

        Returns:
            Tuple[int, int, int]: The best move cost, x, y
        """

        # Player 'O' is max, in this case AI
        # Possible values for maxv are:
        # -1 - loss
        # 0  - a tie
        # 1  - win

        # We're initially setting it to -2 as worse than the worst case:
        maxv = -2

        px = None
        py = None

        result = self.is_end()

        # If the game came to an end, the function needs to return
        # the evaluation function of the end. That can be:
        # -1 - loss
        # 0  - a tie
        # 1  - win
        if result == 'X':
            return -1, 0, 0
        elif result == 'O':
            return 1, 0, 0
        elif result == '.':
            return 0, 0, 0

        for i in range(0, self.row):
            for j in range(0, self.col):
                if self.game_board[i][j] == ' ':
                    # On the empty field player 'O' makes a move and calls Min
                    # That's one branch of the game tree.
                    self.game_board[i][j] = 'O'
                    m, _, _ = self.min()
                    # Fixing the maxv value if needed
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    # Setting back the field to empty
                    self.game_board[i][j] = ' '
        return maxv, px, py

    @functools.lru_cache(var)
    def min(self) -> Tuple[int, int, int]:
        """
            Function for the min value calls max recersevly to detrmine the best move for the X player

        Returns:
            Tuple[int, int, int]: The best move cost, x, y
        """

        # Player 'X' is min, in this case human
        # Possible values for minv are:
        # -1 - win
        # 0  - a tie
        # 1  - loss

        # We're initially setting it to 2 as worse than the worst case:
        minv = 2

        qx = None
        qy = None

        result = self.is_end()

        if result == 'X':
            return -1, 0, 0
        elif result == 'O':
            return 1, 0, 0
        elif result == '.':
            return 0, 0, 0

        for i in range(0, self.row):
            for j in range(0, self.col):
                if self.game_board[i][j] == ' ':
                    self.game_board[i][j] = 'X'
                    m, _, _ = self.max()
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.game_board[i][j] = ' '

        return minv, qx, qy

    @functools.lru_cache(var)
    def max_alpha_beta(self, alpha: int, beta: int) -> Tuple[int, int, int]:
        """
            Function for the max value calls min recersevly to detrmine the best move for the O player but with using alphabeta

        Args:
            alpha (int): The alpha value
            beta (int): The beta value

        Returns:
            Tuple[int, int, int]: The best move cost, x, y
        """

        # Player 'O' is max, in this case AI
        maxv = -2
        px = None
        py = None

        result = self.is_end()

        if result == 'X':
            return -1, 0, 0
        elif result == 'O':
            return 1, 0, 0
        elif result == '.':
            return 0, 0, 0

        for i in range(0, self.row):
            for j in range(0, self.col):
                if self.game_board[i][j] == ' ':
                    self.game_board[i][j] = 'O'
                    m, _, _ = self.min_alpha_beta(alpha, beta)
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    self.game_board[i][j] = ' '

                    # Next two ifs in Max and Min are the only difference between regular algorithm and minimax
                    if maxv >= beta:
                        return maxv, px, py

                    if maxv > alpha:
                        alpha = maxv

        return maxv, px, py

    @functools.lru_cache(var)
    def min_alpha_beta(self, alpha: int, beta: int) -> Tuple[int, int, int]:
        """Function for the min value calls max recersevly to detrmine the best move for the X player but with using alphabeta

        Args:
            alpha (int): The alpha value
            beta (int): The beta value

        Returns:
            Tuple[int, int, int]: The best move cost, x, y
        """

        # Player 'X' is min, in this case human
        minv = 2

        qx = None
        qy = None

        result = self.is_end()

        if result == 'X':
            # print(self.game)
            # print(-1)
            return -1, 0, 0
        elif result == 'O':
            # print(self.game)
            # print(1)
            return 1, 0, 0
        elif result == '.':
            # print(self.game)
            # print(0)
            return 0, 0, 0

        for i in range(0, self.row):
            for j in range(0, self.col):
                if self.game_board[i][j] == ' ':
                    self.game_board[i][j] = 'X'
                    m, _, _ = self.max_alpha_beta(alpha, beta)
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.game_board[i][j] = ' '

                    if minv <= alpha:
                        return minv, qx, qy

                    if minv < beta:
                        beta = minv

        return minv, qx, qy

    def best_move(self, player: str) -> Tuple[int, int]:
        """
            The best move to be played by the player or the AI

        Args:
            player (str): X, or O

        Returns:
            Tuple[int, int]: The best move for the player (x, y)
        """
        # If it's player's turn
        if player == 'X':
            start = time.time()
            if self.alphabeta:
                _, qx, qy = self.min_alpha_beta(-2, 2)
            else:
                _, qx, qy = self.min()
            end = time.time()
            print(self.game)
            print('Evaluation time: {}s'.format(round(end - start, 7)))
            print('Playing move: X = {}, Y = {}'.format(qx, qy))

            return qx, qy
        # If it's AI's turn
        else:
            start = time.time()
            if self.alphabeta:
                _, qx, qy = self.max_alpha_beta(-2, 2)
            else:
                _, qx, qy = self.max()
            end = time.time()
            print(self.game)
            print('Evaluation time: {}s'.format(round(end - start, 7)))
            print('Recommended move: X = {}, Y = {}'.format(qx, qy))
            return qx, qy
