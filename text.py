import pygame
import sys
from pygame.color import THECOLORS

def text():
    pygame.font.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('Игра окочена!')
    f1 = pygame.font.Font(None, 55)
    text1 = f1.render('Game Over', True, (250, 0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(THECOLORS['blue'])
        screen.blit(text1, (175, 160))
        pygame.display.update()
