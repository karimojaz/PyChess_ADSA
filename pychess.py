#!/usr/bin/env python3

import pygame
from pygame.locals import *
from gui import *
from pieces import *
from board import *
from moves import *
from AI import *

window = initializeUI()
b = Board()
b.BlackPlayer.isAI = True

displayPiecesOfBoard(window, b)
grabbedPiece = None

running = 1
while running :
    for event in pygame.event.get():
        if event.type is QUIT:
            running = 0
        if b.currentPlayer.isAI:
            ai = BasicAI(Position(b.currentPlayer, b.squares))
            ai.evaluate()
            b.switchPlayers()
            flushBoard(window, b)
        else:
            if event.type is MOUSEBUTTONDOWN:
                if event.button is 1 and clickIsOnTheChessboard(event):
                    xCoord = event.pos[0]
                    yCoord = event.pos[1]
                    if(grabbedPiece is None):
                        p = grabAPiece(xCoord, yCoord, b)
                        if p is not None and p.owner is b.currentPlayer:
                            grabbedPiece = p
                    elif b.getSquareAt(convertFromCoord(xCoord), 7 - convertFromCoord(yCoord)) is not None and grabbedPiece.isMoveLegal(grabbedPiece.square, b.getSquareAt(convertFromCoord(xCoord), 7 - convertFromCoord(yCoord))):
                        if b.getSquareAt(convertFromCoord(xCoord), 7 - convertFromCoord(yCoord)) is not grabbedPiece.square:
                            b.switchPlayers()
                        grabbedPiece.moveTo(b.getSquareAt(convertFromCoord(xCoord), 7 - convertFromCoord(yCoord)))
                        grabbedPiece = None
                        flushBoard(window, b)

            if event.type is MOUSEMOTION and clickIsOnTheChessboard(event):
                x = convertFromCoord(event.pos[0])
                y = 7 - convertFromCoord(event.pos[1])
                if(grabbedPiece is not None and b.getSquareAt(x, y) is not None and grabbedPiece.isMoveLegal(grabbedPiece.square, b.getSquareAt(x, y))):
                    grabbedPiece.xpos = x
                    grabbedPiece.ypos = y
                    window.blit(pygame.image.load("imgres/board.jpg").convert(), (CONST_BOARD_OFFSET, CONST_BOARD_OFFSET))
                    displayPiecesOfBoard(window, b)
