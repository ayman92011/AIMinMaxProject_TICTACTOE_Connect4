import pygame
from typing import List, Tuple
from operator import add
from pygame.event import Event
from rungame import Run_Game
from random import randint


class DrawGameTic:
    def __init__(self, screen: pygame.Surface = None,
                 start_x: int = 0,
                 start_y: int = 0,
                 size_x: int = 600,
                 size_y: int = 600,
                 border: bool = False) -> None:
        """
            Class for creating the tictactoe enterface

        Args:
            screen (pygame.Surface, optional): The screen object to drawon. Defaults to None.
            start_x (int, optional): The x value to start the grid in pixels. Defaults to 0.
            start_y (int, optional): The y value to start the grid in pixels. Defaults to 0.
            size_x (int, optional): The colum size in the grid. Defaults to 600.
            size_y (int, optional): The row size in the grid. Defaults to 600.
            border (bool, optional): Flag for if you want to draw a border for the grid. Defaults to False.
        """
        # Create a screen object if one is not passed
        if screen:
            self.screen: pygame.Surface = screen
        else:
            self.screen: pygame.Surface = pygame.display.set_mode([600, 600])

        self.size_colum = size_x // 3
        self.size_row = size_y // 3
        self.size_x = size_x
        self.size_y = size_y
        self.start_x = start_x
        self.start_y = start_y
        self.rectlist: List[pygame.Rect] = []
        self.font = pygame.font.SysFont(
            "Arial", self.size_colum + self.size_row // 10)

        # Draws the border of the grid
        if border:
            pygame.draw.line(self.screen, (255, 255, 255),
                             (start_x, start_y), (start_x + size_x, start_y), 5)
            pygame.draw.line(self.screen, (255, 255, 255),
                             (start_x, start_y), (start_x, start_y + size_y), 5)
            pygame.draw.line(self.screen, (255, 255, 255),
                             (start_x + size_x, start_y), (start_x + size_x, start_y + size_y), 5)
            pygame.draw.line(self.screen, (255, 255, 255),
                             (start_x, start_y + size_y), (start_x + size_x, start_y + size_y), 5)

        # Draws the lines in the grid
        for i in range(1, 3):
            pygame.draw.line(self.screen, (255, 255, 255),
                             (self.size_colum * i + start_x, start_y),
                             (self.size_colum * i + start_x, start_y + size_y), 5)
            pygame.draw.line(self.screen, (255, 255, 255),
                             (start_x, self.size_row * i + start_y),
                             (start_x + size_x, self.size_row * i + start_y), 5)

        # Create the hit box for each grid box
        for i in range(3):
            for j in range(3):
                self.rectlist.append(pygame.Rect(
                    start_x + self.size_colum * i,
                    start_y + self.size_row * j,
                    self.size_colum,
                    self.size_row))

    def click(self, x: int, y: int) -> int:
        """
            Function to know which square did you press

        Args:
            x (int): The x corrds for the click in pixels
            y (int): The y corrds for the click in pixels

        Returns:
            int: The square pressesd from 0 to 8
        """
        for index, rect in enumerate(self.rectlist):
            if rect.collidepoint(x, y):
                return index

    def update(self, game_board: List[List[int]]) -> None:
        """Function to draw the board on the gui

        Args:
            game_board (List[List[int]]): The game board
        """
        for i in range(len(game_board)):
            for j in range(len(game_board[0])):
                img = self.font.render(
                    game_board[i][j], True, pygame.Color("White"))
                self.screen.blit(
                    img, tuple(map(add, self.rectlist[i + j * 3].topleft, (25, -25))))


class Button:
    def __init__(self, screen: pygame.Surface,
                 text: str,
                 pos: Tuple[int],
                 font_size: int,
                 bgcolor: str = "black",
                 textcolor: str = "White") -> None:
        """
            Class to create a Button in pygame

        Args:
            screen (pygame.Surface): The screen object to draw on.
            text (str): The text displayed on the button
            pos (Tuple[int]): The corrds of the button in format [x, y]
            font_size (int): The font size of the button
            bgcolor (str, optional): The background color of the button. Defaults to "black".
            textcolor (str, optional): The color of the text. Defaults to "White".
        """
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font_size)

        # Create a screen object if one is not passed
        if screen:
            self.screen: pygame.Surface = screen
        else:
            self.screen: pygame.Surface = pygame.display.set_mode([600, 600])

        self.__change_text(text, bgcolor, textcolor)

    def __change_text(self, text: str,
                      bgcolor: str = "black",
                      textcolor: str = "White") -> None:
        """
            Function to change the text of the button

        Args:
            text (str): The text to change to.
            bgcolor (str, optional): The background color of the button. Defaults to "black".
            textcolor (str, optional): The color of the text. Defaults to "White".
        """
        self.text = self.font.render(text, 1, pygame.Color(textcolor))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bgcolor)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self) -> None:
        """
            Draw the button on the screen
        """
        self.screen.blit(self.surface, (self.x, self.y))

    def isClicked(self, event: Event) -> bool:
        """
            Checks if the button is pressed

        Args:
            event (Event): pygame event

        Returns:
            bool: True if the button is pressed
        """
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    # self.change_text(self., bg="red")
                    return True
        return False


class MainScene:
    def __init__(self) -> None:
        """
            Class for the home screen of the GUI
        """
        self.scene = pygame.display.set_mode([600, 600])
        self.AIvsoneButton = Button(self.scene, "Start Single Player Mode player Starts",
                                    (10, 50), 20, "Black")
        self.onevsAIButton = Button(self.scene, "Start Single Player Mode AI starts",
                                    (10, 100), 20, "Black")
        self.MultiButton = Button(self.scene, "Start Multi player Mode",
                                  (10, 150), 20, "Black")
        self.AIvsAIButton = Button(self.scene, "Start AI Mode",
                                   (10, 200), 20, "Black")
        self.scene.fill(pygame.Color("Black"))

    def show(self) -> None:
        """
            Used to update and show the elements on the Screen
        """
        self.onevsAIButton.show()
        self.AIvsoneButton.show()
        self.MultiButton.show()
        self.AIvsAIButton.show()
        pygame.display.flip()

    def handle_event(self, event: Event) -> int:
        """
            Function to handle any event while in the main screen

        Args:
            event (Event): pygame event

        Returns:
            int: The number of button that was pressed and None if nothing is pressed.
        """
        if self.AIvsoneButton.isClicked(event):
            return 0
        if self.onevsAIButton.isClicked(event):
            return 1
        if self.MultiButton.isClicked(event):
            return 2
        if self.AIvsAIButton.isClicked(event):
            return 3
        return None


class TicGameScene:
    def __init__(self, ai: bool = True, ai_goes_first: bool = False, aiall: bool = False) -> None:
        """
            Class for the Tic Game screen in the GUI

        Args:
            ai (bool, optional): Flag to konw if you want to use AI as player. Defaults to True.
            ai_goes_first (bool, optional): Flag to know if you want the AI to go first. Defaults to False.
            aiall (bool, optional): Flag to know if you want AI vs AI mode. Defaults to False.
        """
        self.scene = pygame.display.set_mode([600, 600])
        self.gui = DrawGameTic(self.scene, border=True)
        self.ai = ai
        self.aiall = aiall
        self.game = Run_Game(start=ai_goes_first)

    def show(self) -> None:
        """
            Function to update the game screen in the GUI
        """
        self.gui.update(self.game.game_board)
        pygame.display.flip()

    def handle_event(self, event: Event) -> None:
        """
            Function to handle any event while i the game screen

        Args:
            event (Event): pygame event
        """
        if self.aiall and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if self.game.movesLeft() == 9:
                    x_rand = randint(0, 2)
                    y_rand = randint(0, 2)
                    self.game.run(x_rand, y_rand)
                self.game.run()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            index = self.gui.click(x, y)
            y = index // 3
            x = index % 3
            if self.game.run(x, y):
                if self.ai:
                    self.game.run()
