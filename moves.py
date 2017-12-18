import pieces
import board
import copy

class Move:

    def __init__(self, piece, destSquare):
        self.piece = piece
        self.destSquare = destSquare

    def __str__(self):
        return str(self.piece.square) + " to " + str(self.destSquare)

class Position:

    def __init__(self, player, squares):
        self.player = player
        self.legalMoves = []
        self.squares = squares

    def computePossibleMoves(self):
        for p in self.player.pieceSet.allPieces:
            for s in self.squares:
                if s is not p.square and p.isMoveLegal(p.square, s):
                    capturedPiece = None
                    if s.occupyingPiece is not None and s.occupyingPiece.owner.color is not self.player.color:
                        capturedPiece = s.occupyingPiece
                        self.player.b.getOpponent(self.player).pieceSet.erase(capturedPiece)
                    oldSquare = p.square
                    oldSquare.occupyingPiece = None
                    p.square = s
                    p.square.occupyingPiece = p
                    p.xpos = p.square.xpos
                    p.ypos = p.square.ypos
                    if not self.player.pieceSet.king.isInCheck():
                        self.legalMoves.append(Move(p, s))
                    p.square.occupyingPiece = capturedPiece
                    p.square = oldSquare
                    p.square.occupyingPiece = p
                    p.xpos = p.square.xpos
                    p.ypos = p.square.ypos
                    if capturedPiece is not None:
                        if capturedPiece.owner.color is not self.player.color:
                            self.player.b.getOpponent(self.player).pieceSet.add(capturedPiece)
        return self.legalMoves
