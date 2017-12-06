import pygame
from board import *

class Piece:

    def __init__(self, xpos, ypos, owner):
        self.xpos = xpos
        self.ypos = ypos
        self.square = Square(xpos, ypos)
        self.owner = owner
        self.sprite = None

    def moveTo(newSquare):
        self.square.occupyingPiece = None
        self.square = newSquare

class Pawn(Piece):

    def __init__(self, xpos, ypos, owner):
        Piece.__init__(self, xpos, ypos, owner)
        self.hasMoved = False
        self.sprite = pygame.image.load("imgres/" + ("bp.png" if (self.owner.color == "black") else "wp.png")).convert_alpha()

class Rook(Piece):

    def __init__(self, xpos, ypos):
        Piece.__init__(xpos, ypos)
        self.sprite = pygame.image.load("imgres/" + ("br.png" if (self.owner.color == "black") else "wr.png")).convert_alpha()

class Knight(Piece):

    def __init__(self, xpos, ypos):
        Piece.__init__(xpos, ypos)

class Bishop(Piece):

    def __init__(self, xpos, ypos):
        Piece.__init__(xpos, ypos)

class Queen(Piece):

    def __init__(self, xpos, ypos):
        Piece.__init__(xpos, ypos)

class King(Piece):

    def __init__(self, xpos, ypos):
        Piece.__init__(xpos, ypos)
