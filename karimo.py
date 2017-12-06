#!/usr/bin/env python3

import pygame
from gui import *
from pygame.locals import *

CONST_BOARD_OFFSET = 68
CONST_SQUARE_DIM = 82

def placePieces(window, piece_x, piece_y):
    br = pygame.image.load("imgres/br.png").convert_alpha()
    """bk = pygame.image.load("imgres/bk.jpg").convert()
    bn = pygame.image.load("imgres/bn.jpg").convert()
    br = pygame.image.load("imgres/br.jpg").convert()"""
    br_pos = (piece_x, piece_y)
    window.blit(br, br_pos)
    pygame.display.flip()

def initializeUI():
    pygame.init()
    window = pygame.display.set_mode((1408, 792))
    pygame.display.set_caption('PyChess_ADSA')
    bg = pygame.image.load("imgres/bg.jpg").convert()
    window.blit(bg, (0,0))
    board = pygame.image.load("imgres/board.jpg").convert()
    window.blit(board, (CONST_BOARD_OFFSET, CONST_BOARD_OFFSET))
    pygame.display.flip()
    return window

window = initializeUI()

keepon = 1
while keepon :
    for event in pygame.event.get():
        if event.type == QUIT:
            keepon = 0
        if event.type == MOUSEBUTTONDOWN :
            if event.button == 1 :
                placePieces(window, event.pos[0], event.pos[1])
