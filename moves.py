import pieces
import board

class Move:

    def __init__(self, piece, destSquare):
        self.piece = piece

class Position:

    def __init__(self, squares, player):
        self.squares = squares
        self.player = player
        self.legalMoves = []
