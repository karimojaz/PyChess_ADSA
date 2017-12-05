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
        }[self.xpos] + str(self.ypos+1)

class Player:

    def __init__(self, color):
        self.color = color

class PieceSet:

    def __init__(self, player):
        if player.color == "black":
            pawnRow = 6
        else:
            pawnRow = 1
        for i in range(8):
            self.pawns.append(pawn(i+1, pawnRow))

class Board:

    def __init__(self):
        
