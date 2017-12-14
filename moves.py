import pieces
import board
import copy

class Move:

    def __init__(self, piece, destSquare):
        self.piece = piece
        self.destSquare = destSquare

class Position:

    def __init__(self, player, squares):
        self.player = player
        self.legalMoves = []
        self.squares = copy.deepcopy(squares)

    def computePossibleMoves(self):
        for p in self.player.pieceSet.allPieces:
            for s in self.squares:
                if s is not p.square and p.isMoveLegal(p.square, s):
                    self.legalMoves.append(Move(p, s))
        return self.legalMoves
