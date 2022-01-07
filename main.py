# For Type checking
from typing import Union
# The GUI classes
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

        sceneOb.show()

        if mode_select is not None:
            if mode_select == 0:
                scene.fill((0, 0, 0))
                sceneOb = TicGameScene()
                mode_select = None
            elif mode_select == 1:
                scene.fill((0, 0, 0))
                sceneOb = TicGameScene(ai_goes_first=True)
                mode_select = None
            elif mode_select == 2:
                scene.fill((0, 0, 0))
                sceneOb = TicGameScene(ai=False)
                mode_select = None
            elif mode_select == 3:
                scene.fill((0, 0, 0))
                sceneOb = TicGameScene(aiall=True)
                mode_select = None

    # Done! Time to quit.
    pygame.quit()
