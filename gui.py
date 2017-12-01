import pygame

CONST_VERTICAL_BOARD_OFFSET = 68
CONST_SQUARE_DIM = 82

def initializeUI():
    pygame.init()
    window = pygame.display.set_mode((1408, 792))
    bg = pygame.image.load("imgres/board.jpg").convert()
    window.blit(bg, (0,0 + CONST_VERTICAL_BOARD_OFFSET))
    pygame.display.flip()
