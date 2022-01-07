class Connect4:
    def __init__(self) -> None:
        """
            Create Connect 4 Game logic
        """
        self.connect_board = [[" ", " ", " ", " ", " ", " ", " "],
                              [" ", " ", " ", " ", " ", " ", " "],
                              [" ", " ", " ", " ", " ", " ", " "],
                              [" ", " ", " ", " ", " ", " ", " "],
                              [" ", " ", " ", " ", " ", " ", " "],
                              [" ", " ", " ", " ", " ", " ", " "]]
        self.turn = True

    def play(self, x: int, y: int) -> bool:
        """
            playes one move for each player

        Args:
            x (int): x coords for place to play
            y (int): y coords for place to play

        Returns:
            bool: True if you can play the move else False
        """
        if self.connect_board[x][y] != " ":
            return False
        print(x, y)
        if self.turn:
            self.connect_board[self.check_avalable(y)][y] = "X"
        else:
            self.connect_board[self.check_avalable(y)][y] = "O"
        self.turn = not self.turn
        return True

    def check_avalable(self, y):
        for i in range(5, -1, -1):
            if self.connect_board[i][y] == " ":
                return i

    def isMovesLeft(self) -> bool:
        """
            Checks if any moves is left

        Returns:
            bool: True if there are any left moves
        """
        for i in range(len(self.connect_board)):
            for j in range(len(self.connect_board[0])):
                if (self.connect_board[i][j] == " "):
                    return True
        return False

    def movesLeft(self) -> int:
        """
            Gets the number of moves left

        Returns:
            int: The number of empty cells
        """
        sum = 0
        for i in range(len(self.connect_board)):
            for j in range(len(self.connect_board[0])):
                if (self.connect_board[i][j] == " "):
                    sum += 1
        return sum

    def win(self) -> str:
        """
            Function for when the player wins

        Returns:
            str: player 1 wins or player 2 wins
        """
        win_x = "X wins"
        win_o = "O wins"
        # Check horizontal locations for win
        for c in range(len(self.connect_board[0])-3):
            for r in range(len(self.connect_board)):
                if self.connect_board[r][c] == "X" and self.connect_board[r][c+1] == "X" and self.connect_board[r][c+2] == "X" and self.connect_board[r][c+3] == "X":
                    return win_x
                if self.connect_board[r][c] == "O" and self.connect_board[r][c+1] == "O" and self.connect_board[r][c+2] == "O" and self.connect_board[r][c+3] == "O":
                    return win_o

        # Check vertical locations for win
        for c in range(len(self.connect_board[0])):
            for r in range(len(self.connect_board)-3):
                if self.connect_board[r][c] == "X" and self.connect_board[r+1][c] == "X" and self.connect_board[r+2][c] == "X" and self.connect_board[r+3][c] == "X":
                    return win_x
                if self.connect_board[r][c] == "O" and self.connect_board[r+1][c] == "O" and self.connect_board[r+2][c] == "O" and self.connect_board[r+3][c] == "O":
                    return win_o

        # Check positively sloped diaganols
        for c in range(len(self.connect_board[0])-3):
            for r in range(len(self.connect_board)-3):
                if self.connect_board[r][c] == "X" and self.connect_board[r+1][c+1] == "X" and self.connect_board[r+2][c+2] == "X" and self.connect_board[r+3][c+3] == "X":
                    return win_x
                if self.connect_board[r][c] == "O" and self.connect_board[r+1][c+1] == "O" and self.connect_board[r+2][c+2] == "O" and self.connect_board[r+3][c+3] == "O":
                    return win_o

        # Check negatively sloped diaganols
        for c in range(len(self.connect_board[0])-3):
            for r in range(3, len(self.connect_board)):
                if self.connect_board[r][c] == "X" and self.connect_board[r-1][c+1] == "X" and self.connect_board[r-2][c+2] == "X" and self.connect_board[r-3][c+3] == "X":
                    return win_x
                if self.connect_board[r][c] == "O" and self.connect_board[r-1][c+1] == "O" and self.connect_board[r-2][c+2] == "O" and self.connect_board[r-3][c+3] == "O":
                    return win_o

        if not self.isMovesLeft():
            return "Draw"
        return ""

    def __str__(self) -> str:
        """ToString method to print the class

        Returns:
            str: board in format ['', '', '', '', '', '', '']
                                 ['', '', '', '', '', '', '']
                                 ['', '', '', '', '', '', '']
                                 ['', '', '', '', '', '', '']
                                 ['', '', '', '', '', '', '']
                                 ['', '', '', '', '', '', '']
        """
        return f"{self.connect_board[0]}\n{self.connect_board[1]}\n{self.connect_board[2]}\n{self.connect_board[3]}\n{self.connect_board[4]}\n{self.connect_board[5]}"


if __name__ == "__main__":
    game = Connect4()
    game.connect_board = [[" ", " ", " ", " ", " ", " ", " "],
                          [" ", " ", " ", " ", " ", " ", " "],
                          [" ", " ", " ", " ", " ", " ", " "],
                          [" ", " ", " ", " ", " ", " ", " "],
                          [" ", " ", " ", " ", " ", " ", " "],
                          [" ", " ", " ", " ", " ", " ", " "]]
    print(game.win())
