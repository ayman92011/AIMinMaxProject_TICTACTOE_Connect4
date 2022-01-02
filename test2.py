import pygame as pg
import pygame
pygame.init()
screen = pg.display.set_mode((640, 480))
rect1 = pg.Rect(100, 100, 161, 100)
rect2 = pg.Rect(300, 200, 161, 100)
done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        screen.fill((30, 30, 30))
    pg.draw.rect(screen, (0, 100, 250), rect1)
    pg.draw.rect(screen, (0, 200, 120), rect2)
    font = pygame.font.SysFont(None, 24)
    img = font.render('hello', True, pygame.Color("Blue"))
    screen.blit(img, (20, 20))
    pg.display.flip()
