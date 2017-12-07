#!/usr/bin/env python3

import pygame
from pygame.locals import *
from gui import *
from pieces import *
from board import *

window = initializeUI()

b = Board()
displayPiecesOfBoard(window, b)
grabbedPiece = None

running = 1
while running :
    for event in pygame.event.get():
        if event.type == QUIT:
            running = 0

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1 and clickIsOnTheChessboard(event):
                if(grabbedPiece == None):
                    grabbedPiece = grabAPiece(event.pos[0], event.pos[1], b)
                else:
                    grabbedPiece.moveTo(b.getSquareAt(convertFromCoord(event.pos[0]), 7 - convertFromCoord(event.pos[1])))
                    grabbedPiece = None
                    flushBoard(window, b)

        if event.type == MOUSEMOTION and clickIsOnTheChessboard(event):
            if(grabbedPiece != None):
                grabbedPiece.xpos = convertFromCoord(event.pos[0])
                grabbedPiece.ypos = 7 - convertFromCoord(event.pos[1])
                flushBoard(window, b)
