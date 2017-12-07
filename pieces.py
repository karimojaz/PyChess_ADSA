import pygame
import board

class Piece:

    def __init__(self, xpos, ypos, owner):
        self.xpos = xpos
        self.ypos = ypos
        self.square = board.Square(xpos, ypos)
        self.owner = owner
        self.sprite = None

    def moveTo(self, newSquare):
        self.square.occupyingPiece = None
        self.square = newSquare
        self.square.occupyingPiece = self
        self.xpos = self.square.xpos
        self.ypos = self.square.ypos

class Pawn(Piece):

    def __init__(self, xpos, ypos, owner):
        Piece.__init__(self, xpos, ypos, owner)
        self.hasMoved = False
        self.sprite = pygame.image.load("imgres/" + ("bp.png" if (self.owner.color == "black") else "wp.png")).convert_alpha()

class Rook(Piece):

    def __init__(self, xpos, ypos, owner):
        Piece.__init__(self, xpos, ypos, owner)
        self.sprite = pygame.image.load("imgres/" + ("br.png" if (self.owner.color == "black") else "wr.png")).convert_alpha()

class Knight(Piece):

    def __init__(self, xpos, ypos, owner):
        Piece.__init__(self, xpos, ypos, owner)
        self.sprite = pygame.image.load("imgres/" + ("bn.png" if (self.owner.color == "black") else "wn.png")).convert_alpha()

class Bishop(Piece):

    def __init__(self, xpos, ypos, owner):
        Piece.__init__(self, xpos, ypos, owner)
        self.sprite = pygame.image.load("imgres/" + ("bb.png" if (self.owner.color == "black") else "wb.png")).convert_alpha()

class Queen(Piece):

    def __init__(self, xpos, ypos, owner):
        Piece.__init__(self, xpos, ypos, owner)
        self.sprite = pygame.image.load("imgres/" + ("bq.png" if (self.owner.color == "black") else "wq.png")).convert_alpha()

class King(Piece):

    def __init__(self, xpos, ypos, owner):
        Piece.__init__(self, xpos, ypos, owner)
        self.sprite = pygame.image.load("imgres/" + ("bk.png" if (self.owner.color == "black") else "wk.png")).convert_alpha()
