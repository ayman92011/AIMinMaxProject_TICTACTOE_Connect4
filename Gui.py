import pygame
from typing import List
from operator import add


class DrawGameTic:
    def __init__(self, screen: pygame.Surface = None,
                 start_x: int = 0,
                 start_y: int = 0,
                 size_x: int = 600,
                 size_y: int = 600,
                 border: bool = False) -> None:
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

        if border:
            pygame.draw.line(self.screen, (255, 255, 255),
                             (start_x, start_y), (start_x + size_x, start_y), 5)
            pygame.draw.line(self.screen, (255, 255, 255),
                             (start_x, start_y), (start_x, start_y + size_y), 5)
            pygame.draw.line(self.screen, (255, 255, 255),
                             (start_x + size_x, start_y), (start_x + size_x, start_y + size_y), 5)
            pygame.draw.line(self.screen, (255, 255, 255),
                             (start_x, start_y + size_y), (start_x + size_x, start_y + size_y), 5)

        for i in range(1, 3):
            pygame.draw.line(self.screen, (255, 255, 255),
                             (self.size_colum * i + start_x, start_y),
                             (self.size_colum * i + start_x, start_y + size_y), 5)
            pygame.draw.line(self.screen, (255, 255, 255),
                             (start_x, self.size_row * i + start_y),
                             (start_x + size_x, self.size_row * i + start_y), 5)

        for i in range(3):
            for j in range(3):
                self.rectlist.append(pygame.Rect(
                    start_x + self.size_colum * i,
                    start_y + self.size_row * j,
                    self.size_colum,
                    self.size_row))

    def click(self, x, y) -> int:
        for index, rect in enumerate(self.rectlist):
            if rect.collidepoint(x, y):
                return index

    def update(self, game_board):
        for i in range(len(game_board)):
            for j in range(len(game_board[0])):
                # self.put_text(game_board[i][j], self.rectlist[i + j * 3])
                img = self.font.render(
                    game_board[i][j], True, pygame.Color("White"))
                self.screen.blit(
                    img, tuple(map(add, self.rectlist[i + j * 3].topleft, (25, -25))))
