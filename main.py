from typing import Union
from Gui import MainScene, TicGameScene

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
sceneOb: Union[MainScene, TicGameScene] = MainScene()
scene = sceneOb.scene


if __name__ == "__main__":
    running = True
    mode_select = None
    while running:

        for event in pygame.event.get():
            mode_select = sceneOb.handle_event(event)
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        sceneOb.update()
        sceneOb.show()

        if mode_select is not None:
            scene.fill((0, 0, 0))
            sceneOb = TicGameScene()
            mode_select = None

    # Done! Time to quit.
    pygame.quit()
