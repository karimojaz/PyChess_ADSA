import pygame
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((1024, 720))
bg = pygame.image.load("imgres/board.jpg").convert()
window.blit(bg, (0,0))
pygame.display.flip()

while(1):
    continue
