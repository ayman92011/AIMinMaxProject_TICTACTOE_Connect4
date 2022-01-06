#!/usr/bin/env python3
from math import inf as infinity
from random import choice
import platform
import time
from os import system
from typing import Union
from TicTacToeLogic import TicTacToe
from Connect4Logic import Connect4


class MinMaxAI:
    HUMAN = -1
    COMP = +1

    def __init__(self, h_choice, c_choice, game: Union[TicTacToe, Connect4] = None) -> None:
        if not game:
            game = TicTacToe()
        else:
            self.game = game
        self.game_board = self.game.tic_board
        self.chars = {
            -1: c_choice,
            +1: h_choice,
            0: ' '
        }
        if c_choice == "O":
            self.current = MinMaxAI.HUMAN
        else:
            print("here")
            self.current = MinMaxAI.COMP

    def evaluate(self):
        """
        Function to heuristic evaluation of state.
        :param state: the state of the current board
        :return: +1 if the computer wins; -1 if the human wins; 0 draw
        """
        if self.game.win(MinMaxAI.COMP):
            score = +1
        elif self.game.win(MinMaxAI.HUMAN):
            score = -1
        else:
            score = 0

        return score

    def game_over(self):
        """
        This function test if the human or computer wins
        :param state: the state of the current board
        :return: True if the human or computer wins
        """
        return self.game.win(MinMaxAI.HUMAN) or self.game.win(MinMaxAI.COMP)

    def empty_cells(self):
        """
        Each empty cell will be added into cells' list
        :param state: the state of the current board
        :return: a list of empty cells
        """
        cells = []

        for x, row in enumerate(self.game_board):
            for y, cell in enumerate(row):
                if cell == " ":
                    cells.append([x, y])

        return cells

    def minimax(self, depth, player):
        """
        AI function that choice the best move
        :param state: current state of the board
        :param depth: node index in the tree (0 <= depth <= 9),
        but never nine in this case (see iaturn() function)
        :param player: an human or a computer
        :return: a list with [the best row, best col, best score]
        """
        if player == MinMaxAI.COMP:
            best = [-1, -1, -infinity]
        else:
            best = [-1, -1, +infinity]

        if depth == 0 or self.game_over():
            score = self.evaluate()
            return [-1, -1, score]

        for cell in self.empty_cells():
            x, y = cell[0], cell[1]
            self.game_board[x][y] = self.chars[player]
            score = self.minimax(depth - 1, -player)
            self.game_board[x][y] = self.chars[0]
            score[0], score[1] = x, y

            if player == MinMaxAI.COMP:
                # print(best, score)
                if score[2] > best[2]:
                    best = score  # max value
                # print(best, score)
            else:
                if score[2] < best[2]:
                    best = score  # min value

        return best

    def ai_play(self):
        """
        It calls the minimax function if the depth < 9,
        else it choices a random coordinate.
        :param c_choice: computer's choice X or O
        :param h_choice: human's choice X or O
        :return:
        """
        depth = len(self.empty_cells())
        if depth == 0 or self.game_over():
            return

        print(f'Computer turn [{self.chars[-1]}]')

        if depth == -1:
            x = choice([0, 1, 2])
            y = choice([0, 1, 2])
        else:
            move = self.minimax(depth, MinMaxAI.HUMAN)
            x, y = move[0], move[1]
            print(move)

        # self.game.play(x, y)
        return x, y


# def main():
#     """
#     Main function that calls all functions
#     """
#     clean()
#     h_choice = ''  # X or O
#     c_choice = ''  # X or O
#     first = ''  # if human is the first

#     # Human chooses X or O to play
#     while h_choice != 'O' and h_choice != 'X':
#         try:
#             print('')
#             h_choice = input('Choose X or O\nChosen: ').upper()
#         except (EOFError, KeyboardInterrupt):
#             print('Bye')
#             exit()
#         except (KeyError, ValueError):
#             print('Bad choice')

#     # Setting computer's choice
#     if h_choice == 'X':
#         c_choice = 'O'
#     else:
#         c_choice = 'X'

#     # Human may starts first
#     clean()
#     while first != 'Y' and first != 'N':
#         try:
#             first = input('First to start?[y/n]: ').upper()
#         except (EOFError, KeyboardInterrupt):
#             print('Bye')
#             exit()
#         except (KeyError, ValueError):
#             print('Bad choice')

#     # Main loop of this game
#     while len(empty_cells(board)) > 0 and not game_over(board):
#         if first == 'N':
#             ai_turn(c_choice, h_choice)
#             first = ''

#         human_turn(c_choice, h_choice)
#         ai_turn(c_choice, h_choice)

#     # Game over message
#     if wins(board, HUMAN):
#         clean()
#         print(f'Human turn [{h_choice}]')
#         render(board, c_choice, h_choice)
#         print('YOU WIN!')
#     elif wins(board, COMP):
#         clean()
#         print(f'Computer turn [{c_choice}]')
#         render(board, c_choice, h_choice)
#         print('YOU LOSE!')
#     else:
#         clean()
#         render(board, c_choice, h_choice)
#         print('DRAW!')

#     exit()


if __name__ == '__main__':
    pass
