import time
from typing import Union
from Connect4Logic import Connect4
from TicTacToeLogic import TicTacToe


class MinMaxAI:
    def __init__(self, game: Union[TicTacToe, Connect4] = None) -> None:
        if not game:
            game = TicTacToe()
        else:
            self.game = game
        self.game_board = self.game.tic_board

    # Determines if the made move is a legal move
    def is_valid(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.game_board[px][py] != ' ':
            return False
        else:
            return True

    # Checks if the game has ended and returns the winner in each case
    def is_end(self):
        # # Vertical win
        # for i in range(0, 3):
        #     if (self.current_state[0][i] != '.' and
        #         self.current_state[0][i] == self.current_state[1][i] and
        #             self.current_state[1][i] == self.current_state[2][i]):
        #         return self.current_state[0][i]

        # # Horizontal win
        # for i in range(0, 3):
        #     if (self.current_state[i] == ['X', 'X', 'X']):
        #         return 'X'
        #     elif (self.current_state[i] == ['O', 'O', 'O']):
        #         return 'O'
        if self.game.win() == "X wins":
            return "X"
        elif self.game.win() == "O wins":
            return "O"
        elif self.game.win() == "Draw":
            return "."

        return None
        # # Main diagonal win
        # if (self.current_state[0][0] != '.' and
        #     self.current_state[0][0] == self.current_state[1][1] and
        #         self.current_state[0][0] == self.current_state[2][2]):
        #     return self.current_state[0][0]

        # # Second diagonal win
        # if (self.current_state[0][2] != '.' and
        #     self.current_state[0][2] == self.current_state[1][1] and
        #         self.current_state[0][2] == self.current_state[2][0]):
        #     return self.current_state[0][2]

        # # Is whole board full?
        # for i in range(0, 3):
        #     for j in range(0, 3):
        #         # There's an empty field, we continue the game
        #         if (self.current_state[i][j] == '.'):
        #             return None

        # # It's a tie!
        # return '.'

    # Player 'O' is max, in this case AI
    def max(self):

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

        for i in range(0, 3):
            for j in range(0, 3):
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

    # Player 'X' is min, in this case human
    def min(self):

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

        for i in range(0, 3):
            for j in range(0, 3):
                if self.game_board[i][j] == ' ':
                    self.game_board[i][j] = 'X'
                    m, _, _ = self.max()
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.game_board[i][j] = ' '

        return minv, qx, qy

    def best_move(self, player):
        self.game_board = self.game.tic_board
        # If it's player's turn
        if player == 'X':
            start = time.time()
            _, qx, qy = self.min()
            end = time.time()
            print(self.game)
            print('Evaluation time: {}s'.format(round(end - start, 7)))
            print('Playing move: X = {}, Y = {}'.format(qx, qy))

            return qx, qy
        # If it's AI's turn
        else:
            start = time.time()
            _, qx, qy = self.max()
            end = time.time()
            print(self.game)
            print('Evaluation time: {}s'.format(round(end - start, 7)))
            print('Recommended move: X = {}, Y = {}'.format(qx, qy))
            return qx, qy
