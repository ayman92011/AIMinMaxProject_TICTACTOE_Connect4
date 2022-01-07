class TicTacToe:
    def __init__(self) -> None:
        """
            Create TicTacToe Game logic
        """
        self.tic_board = [[" ", " ", " "],
                          [" ", " ", " "],
                          [" ", " ", " "]]
        self.turn = True

    def play(self, x: int, y: int) -> bool:
        """
            Playes one move for each player

        Args:
            x (int): x coords for place to play
            y (int): y coords for place to play

        Returns:
            bool: True if you can play the move else False
        """
        if self.tic_board[x][y] != " ":
            return False
        if self.turn:
            self.tic_board[x][y] = "X"
        else:
            self.tic_board[x][y] = "O"
        self.turn = not self.turn
        return True

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

    def movesLeft(self) -> int:
        """
            Gets the number of moves left

        Returns:
            int: The number of empty cells
        """
        sum = 0
        for i in range(len(self.tic_board)):
            for j in range(len(self.tic_board[0])):
                if (self.tic_board[i][j] == " "):
                    sum += 1
        return sum

    def win(self) -> str:
        """
            Function for when the player wins

        Returns:
            str: player 1 wins or player 2 wins
        """
        check_x = ["X", "X", "X"]
        check_o = ["O", "O", "O"]
        win_x = "X wins"
        win_o = "O wins"
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
        if not self.isMovesLeft():
            return "Draw"
        return ""

    def __str__(self) -> str:
        """ToString method to print the class

        Returns:
            str: board in format ['', '', '']
                                 ['', '', '']
                                 ['', '', '']
        """
        return f"{self.tic_board[0]}\n{self.tic_board[1]}\n{self.tic_board[2]}"


# Testing the TicTacToe class for bugs
if __name__ == "__main__":
    game = TicTacToe()
    game.tic_board = [
        ['X', 'O', 'O'],
        ['X', 'O', 'O'],
        ['X', 'X', 'X']]
    print(game)
    print(game.win())
