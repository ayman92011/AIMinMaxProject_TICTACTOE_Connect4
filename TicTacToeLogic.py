class TicTacToe:
    def __init__(self) -> None:
        """
            Create TicTacToe Game logic
        """
        self.tic_board = [[" ", " ", " "],
                          [" ", " ", " "],
                          [" ", " ", " "]]
        self.turn = True

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
            return self.tic_board
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
