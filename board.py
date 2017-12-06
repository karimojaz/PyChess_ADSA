from pieces import *

class Square:

    def __init__(self, xpos, ypos):
        self.occupyingPiece = None
        self.xpos = xpos
        self.ypos = ypos

    def __str__(self):
        return {
            0 : 'a',
            1 : 'b',
            2 : 'c',
            3 : 'd',
            4 : 'e',
            5 : 'f',
            6 : 'g',
            7 : 'h'
        } [self.xpos] + str(self.ypos+1)

class Player:

    def __init__(self, color):
        self.color = color
        self.pieceSet = PieceSet(self)

class PieceSet:

    def __init__(self, player):
        self.pawns = []
        for i in range(8):
            self.pawns.append(Pawn(i+1, 6 if (player.color == "black") else 1, player))

class Board:

    def __init__(self):
        self.squares = []
        for x in range(8):
            for y in range(8):
                self.squares.append(Square(x, y))

    def __str__(self):
        for s in self.squares:
            print(str(s) + " -> " + str(s.occupyingPiece))
