from rungame import Run_Game
# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([600, 600])


class DrawGame:


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
        pygame.draw.line(screen, (255, 255, 255), (200, 0), (200, 600), 5)
        pygame.draw.line(screen, (255, 255, 255), (400, 0), (400, 600), 5)
        pygame.draw.line(screen, (255, 255, 255), (0, 200), (600, 200), 5)
        pygame.draw.line(screen, (255, 255, 255), (0, 400), (600, 400), 5)
        rectlist = []
        rectlist.append(pygame.Rect(0, 0, 200, 200))
        rectlist.append(pygame.Rect(200, 0, 200, 200))
        rectlist.append(pygame.Rect(400, 0, 200, 200))
        rectlist.append(pygame.Rect(0, 200, 200, 200))
        rectlist.append(pygame.Rect(200, 200, 200, 200))
        rectlist.append(pygame.Rect(400, 200, 200, 200))
        rectlist.append(pygame.Rect(0, 400, 200, 200))
        rectlist.append(pygame.Rect(200, 400, 200, 200))
        rectlist.append(pygame.Rect(400, 400, 200, 200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for i, v in enumerate(rectlist):
                    if v.collidepoint(x, y):
                        x = i // 3
                        y = i % 3
                        game.run(x, y)
                        # game.run()

        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()
