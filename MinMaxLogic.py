from TicTacToeLogic import TicTacToe


class MinMaxAI:
    def __init__(self, player: str, game: object = None) -> None:
        if not game:
            game = TicTacToe()
        self.game = game
        self.game_board = self.game.tic_board
        self.player = player
        if self.player == "X":
            self.wanttowin = "Player 1 wins"
            self.opponent = "O"
            self.isMax = True
        else:
            self.wanttowin = "Player 2 wins"
            self.opponent = "X"
            self.isMax = False

    def isMovesLeft(self):
        return self.game.isMovesLeft()

    def evaluate(self):
        stat = self.game.win()
        if stat == self.wanttowin:
            return 10
        if stat == "":
            return 0
        return -10

    def minimax(self, depth):
        score = self.evaluate()

        # If Maximizer has won the game return his/her
        # evaluated score
        if (score == 10):
            return score

        # If Minimizer has won the game return his/her
        # evaluated score
        if (score == -10):
            return score

        # If there are no more moves and no winner then
        # it is a tie
        if (self.isMovesLeft() == False):
            return 0

        # If this maximizer's move
        if (self.isMax):
            best = -1000

            # Traverse all cells
            for i in range(len(self.game_board)):
                for j in range(len(self.game_board[0])):

                    # Check if cell is empty
                    if (self.game_board[i][j] == ' '):

                        # Make the move
                        self.game_board[i][j] = self.player

                        # Call minimax recursively and choose
                        # the maximum value
                        self.isMax = not self.isMax
                        best = max(best, self.minimax(depth + 1))

                        # Undo the move
                        self.game_board[i][j] = ' '
            return best
        # If this minimizer's move
        else:
            best = 1000

            # Traverse all cells
            for i in range(len(self.game_board)):
                for j in range(len(self.game_board[0])):

                    # Check if cell is empty
                    if (self.game_board[i][j] == ' '):

                        # Make the move
                        self.game_board[i][j] = self.opponent

                        # Call minimax recursively and choose
                        # the minimum value
                        self.isMax = not self.isMax
                        best = min(best, self.minimax(depth + 1))

                        # Undo the move
                        self.game_board[i][j] = ' '
            return best

    def findBestMove(self):
        bestVal = -1000
        bestMove = (-1, -1)

        # Traverse all cells, evaluate minimax function for
        # all empty cells. And return the cell with optimal
        # value.
        for i in range(len(self.game_board)):
            for j in range(len(self.game_board[0])):

                # Check if cell is empty
                if (self.game_board[i][j] == ' '):

                    # Make the move
                    self.game_board[i][j] = self.player

                    # compute evaluation function for this
                    # move.
                    moveVal = self.minimax(0)

                    # Undo the move
                    self.game_board[i][j] = ' '

                    # If the value of the current move is
                    # more than the best value, then update
                    # best/
                    if (moveVal > bestVal):
                        bestMove = (i, j)
                        bestVal = moveVal

        print(f"The value of the best Move for {self.player} is :", bestMove)
        print()
        return bestMove
