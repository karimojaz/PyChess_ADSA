from pieces import *

class Player:
    def __init__(self, color):
        self.color = color

class PieceSet:
    def __init__(self, player):
        if player.color == "black":
            pawnRow = 7
        else:
            pawnRow = 2
        for i in range(8):
            self.pawns.append(pawn(i+1, pawnRow))
