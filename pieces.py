from board import *

class Piece:

    def __init__(self, xpos, ypos, owner):
        self.xpos = xpos
        self.ypos = ypos
        self.square = Square(xpos, ypos)
        self.owner = owner

    def moveTo(newSquare):
        self.square.occupyingPiece = None
        self.square = newSquare

class Pawn(Piece):

    def __init__(self, xpos, ypos):
        Piece.__init__(xpos, ypos)
        self.hasMoved = False

class Rook(Piece):

    def __init__(self, xpos, ypos):
        Piece.__init__(xpos, ypos)

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
