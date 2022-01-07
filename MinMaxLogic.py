# To know how much time pass in each search for the best move
import time
# For Type checking
from typing import Tuple, Union
# The Connect4 Logic class
from Connect4Logic import Connect4
# The TicTacToe Logic class
from TicTacToeLogic import TicTacToe
import functools
var = 1000


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
            # self.game_board = tuple([tuple(self.game.tic_board[0]),
            #                         tuple(self.game.tic_board[1]),
            #                         tuple(self.game.tic_board[2])])
            self.row = self.col = 3
        else:
            self.game_board = self.game.connect_board
            self.row = 6
            self.col = 7
        self.alphabeta = alphabeta
        self.time_list = []

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

    def ignore_unhashable(func):
        uncached = func.__wrapped__
        attributes = functools.WRAPPER_ASSIGNMENTS + \
            ('cache_info', 'cache_clear')

        @functools.wraps(func, assigned=attributes)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except TypeError as error:
                if 'unhashable type' in str(error):
                    return uncached(*args, **kwargs)
                raise
        wrapper.__uncached__ = uncached
        return wrapper

    @ignore_unhashable
    @ functools.lru_cache(var)
    def minmax(self, game_board, isMax: bool) -> Tuple[int, int, int]:
        # print(game_board)
        # game_board = list((list(game_board[0]),
        #                    list(game_board[1]),
        #                    list(game_board[2])))
        if isMax:
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
                    if game_board[i][j] == ' ':
                        # On the empty field player 'O' makes a move and calls Min
                        # That's one branch of the game tree.
                        game_board[i][j] = 'O'
                        m, _, _ = self.minmax(game_board, False)
                        # Fixing the maxv value if needed
                        if m > maxv:
                            maxv = m
                            px = i
                            py = j
                        # Setting back the field to empty
                        game_board[i][j] = ' '
            return maxv, px, py
        else:

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
                    if game_board[i][j] == ' ':
                        game_board[i][j] = 'X'
                        m, _, _ = self.minmax(game_board, True)
                        if m < minv:
                            minv = m
                            qx = i
                            qy = j
                        game_board[i][j] = ' '

            return minv, qx, qy

    @ignore_unhashable
    @ functools.lru_cache(var)
    def minmaxalphabeta(self, game_board, isMax, alpha, beta):

        if isMax:

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
                    if game_board[i][j] == ' ':
                        game_board[i][j] = 'O'
                        m, _, _ = self.minmaxalphabeta(
                            game_board, False, alpha, beta)
                        if m > maxv:
                            maxv = m
                            px = i
                            py = j
                        game_board[i][j] = ' '

                        # Next two ifs in Max and Min are the only difference between regular algorithm and minimax
                        if maxv >= beta:
                            return maxv, px, py

                        if maxv > alpha:
                            alpha = maxv

            return maxv, px, py
        else:

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
                    if game_board[i][j] == ' ':
                        game_board[i][j] = 'X'
                        m, _, _ = self.minmaxalphabeta(
                            game_board, True, alpha, beta)
                        if m < minv:
                            minv = m
                            qx = i
                            qy = j
                        game_board[i][j] = ' '

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
        # self.game_board = tuple([tuple(self.game.tic_board[0]),
        #                         tuple(self.game.tic_board[1]),
        #                         tuple(self.game.tic_board[2])])
        # If it's player's turn
        if player == 'X':
            start = time.time()
            if self.alphabeta:
                _, qx, qy = self.minmaxalphabeta(self.game_board, False, -2, 2)
            else:
                _, qx, qy = self.minmax(self.game_board, False)
            end = time.time()
            # print(self.game)
            self.time_list.append(end - start)
            print('Evaluation time: {}s'.format(round(end - start, 7)))
            print('Playing move: X = {}, Y = {}'.format(qx, qy))
            print(sum(self.time_list))

            return qx, qy
        # If it's AI's turn
        else:
            start = time.time()
            if self.alphabeta:
                _, qx, qy = self.minmaxalphabeta(self.game_board, True, -2, 2)
            else:
                _, qx, qy = self.minmax(tuple(self.game_board), True)
            end = time.time()
            # print(self.game)
            self.time_list.append(end - start)
            print('Evaluation time: {}s'.format(round(end - start, 7)))
            print('Recommended move: X = {}, Y = {}'.format(qx, qy))
            print(sum(self.time_list))
            return qx, qy
