from rungame import Run_Game
from Gui import DrawGameTic

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([600, 600])


if __name__ == "__main__":
    game = Run_Game()
    # while not game.isWin():
    #     x = int(input("Enter x: "))
    #     y = int(input("Enter y: "))
    #     print(game.run(x, y))
    #     print(game.run())
    # print(game.game.win())
    running = True
    while running:
        screen.fill((0, 0, 0))
        # gui = DrawGameTic(screen, start_x=100, start_y=50, border=True)
        gui = DrawGameTic(screen, border=True)
        gui.update(game.game.tic_board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                index = gui.click(x, y)
                y = index // 3
                x = index % 3
                print(x, y)
                game.run(x, y)
                #         # game.run()

        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()
