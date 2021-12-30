class TicTacToe:
    def __init__(self) -> None:
        """
            Create TicTacToe Game logic
        """
        self.tic_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.turn = 1

    def play(self, x: int, y: int) -> list:
        """ 
            playes one move for each player

        Args:
            x (int): x coords for place to play
            y (int): y coords for place to play

        Raises:
            Exception: place entered twice

        Returns:
            list: playing board
        """
        if self.tic_board[x][y] != " ":
            raise Exception("enter valued place")
        if self.turn:
            self.tic_board[x][y] = "X"
        else:
            self.tic_board[x][y] = "O"
        self.turn = not self.turn
        return self.tic_board

    def isMovesLeft(self) -> bool:
        """
            Checks if any moves is left

        Returns:
            bool: True if there are any left moves
        """
        for i in range(len(self.tic_board)):
            for j in range(len(self.tic_board[0])):
                if (self.tic_board[i][j] == " "):
                    return True
        return False

    def win(self) -> str:
        """
            Function for when the player wins

        Returns:
            str: player 1 wins or player 2 wins
        """
        check_x = ["X", "X", "X"]
        check_o = ["O", "O", "O"]
        win_x = "Player 1 wins"
        win_o = "Player 2 wins"
        if not self.isMovesLeft():
            return "Draw"
        for i in range(3):
            # check for horizontal wins
            if self.tic_board[i] == check_x:
                return win_x
            if self.tic_board[i] == check_o:
                return win_o
            # check for vertical wins
            if [row[i] for row in self.tic_board] == check_x:
                return win_x
            if [row[i] for row in self.tic_board] == check_o:
                return win_o
        # check for diagonals
        if [self.tic_board[i1][i1] for i1 in range(len(self.tic_board))] == check_x:
            return win_x
        if [self.tic_board[i1][i1] for i1 in range(len(self.tic_board))] == check_o:
            return win_o
        if [self.tic_board[i][len(self.tic_board[0])-i-1] for i in range(len(self.tic_board))] == check_x:
            return win_x
        if [self.tic_board[i][len(self.tic_board[0])-i-1] for i in range(len(self.tic_board))] == check_o:
            return win_o

        return ""

    def __str__(self) -> str:
        return f"{self.tic_board[0]}\n{self.tic_board[1]}\n{self.tic_board[2]}"


class Connect4:
    def __init__(self) -> None:
        self.connect_board = [[" ", " ", " ", " ", " ", " ", " "],
                              [" ", " ", " ", " ", " ", " ", " "],
                              [" ", " ", " ", " ", " ", " ", " "],
                              [" ", " ", " ", " ", " ", " ", " "],
                              [" ", " ", " ", " ", " ", " ", " "],
                              [" ", " ", " ", " ", " ", " ", " "]]


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
            self.isMax = False
        else:
            self.wanttowin = "Player 2 wins"
            self.opponent = "X"
            self.isMax = True

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
