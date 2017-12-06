#!/usr/bin/env python3

import pygame
from pygame.locals import *
from gui import *
from pieces import *

window = initializeUI()

keepon = 1
while keepon :
    for event in pygame.event.get():
        if event.type == QUIT:
            keepon = 0
        if event.type == MOUSEBUTTONDOWN :
            if event.button == 1 :
                putSprite(window, Pawn(event.pos[0], event.pos[1], Player("white")))
