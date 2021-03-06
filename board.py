import pieces
import moves

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
        } [self.xpos] + str(self.ypos+1) + " -> " + str(self.occupyingPiece) + "\n"

    def isFree(self):
        return self.occupyingPiece is None

class Player:

    def __init__(self, color, b):
        self.color = color
        self.pieceSet = PieceSet(self)
        self.capturedPieces = []
        self.b = b
        self.isAI = False

    def getControlledSquares(self):
        cs = []
        for p in self.pieceSet.getAllPieces():
            for s in self.b.squares:
                if s not in cs and p.controls(s):
                    cs.append(s)
        return cs

class PieceSet:

    def __init__(self, player):
        self.king = pieces.King(4, 7 if (player.color == "black") else 0, player)
        self.queen = pieces.Queen(3, 7 if (player.color == "black") else 0, player)
        self.pawns = []
        self.knights = []
        self.bishops = []
        self.rooks = []
        self.knights.append(pieces.Knight(1, 7 if (player.color == "black") else 0, player))
        self.knights.append(pieces.Knight(6, 7 if (player.color == "black") else 0, player))
        self.bishops.append(pieces.Bishop(2, 7 if (player.color == "black") else 0, player))
        self.bishops.append(pieces.Bishop(5, 7 if (player.color == "black") else 0, player))
        self.rooks.append(pieces.Rook(0, 7 if (player.color == "black") else 0, player))
        self.rooks.append(pieces.Rook(7, 7 if (player.color == "black") else 0, player))
        for i in range(8):
            self.pawns.append(pieces.Pawn(i, 6 if (player.color == "black") else 1, player))
        self.allPieces = self.pawns + self.bishops + self.knights + self.rooks + [self.queen, self.king]

    def add(self, p):
        if isinstance(p, pieces.King):
            self.king = p
        elif isinstance(p, pieces.Queen):
            self.queen = p
        elif isinstance(p, pieces.Pawn):
            self.pawns.append(p)
        elif isinstance(p, pieces.Knight):
            self.knights.append(p)
        elif isinstance(p, pieces.Bishop):
            self.bishops.append(p)
        elif isinstance(p, pieces.Rook):
            self.rooks.append(p)

    def erase(self, p):
        if isinstance(p, pieces.King):
            self.king = None
        elif isinstance(p, pieces.Queen):
            self.queen = None
        elif isinstance(p, pieces.Pawn):
            self.pawns.remove(p)
        elif isinstance(p, pieces.Knight):
            self.knights.remove(p)
        elif isinstance(p, pieces.Bishop):
            self.bishops.remove(p)
        elif isinstance(p, pieces.Rook):
            self.rooks.remove(p)
        self.updateAllPiecesCollection()
        for p in self.allPieces:
            if p is None:
                self.allPieces.remove(p)

    def updateAllPiecesCollection(self):
        self.allPieces = self.pawns + self.bishops + self.knights + self.rooks
        if self.queen is not None:
            self.allPieces = self.allPieces + [self.queen]
        if self.king is not None:
            self.allPieces = self.allPieces + [self.king]

    def getAllPieces(self):
        self.updateAllPiecesCollection()
        return self.allPieces

class Board:

    def __init__(self):
        self.WhitePlayer = Player("white", self)
        self.BlackPlayer = Player("black", self)
        self.squares = []
        self.currentPlayer = self.WhitePlayer

        for x in range(8):
            for y in range(8):
                self.squares.append(Square(x, y))

        for p in self.WhitePlayer.pieceSet.allPieces:
            self.getSquareAt(p.xpos, p.ypos).occupyingPiece = p
            p.square = self.getSquareAt(p.xpos, p.ypos)

        for p in self.BlackPlayer.pieceSet.allPieces:
            self.getSquareAt(p.xpos, p.ypos).occupyingPiece = p
            p.square = self.getSquareAt(p.xpos, p.ypos)

    def __str__(self):
        result = ""
        for s in self.squares:
            result += str(s)
        return result

    def getSquareAt(self, xpos, ypos):
        for s in self.squares:
            if(s.xpos == xpos and s.ypos == ypos):
                return s

    def switchPlayers(self):
        self.currentPlayer = self.WhitePlayer if (self.currentPlayer is self.BlackPlayer) else self.BlackPlayer

    def getPosition(self):
        return moves.Position(self.squares, self.currentPlayer)

    def getOpponent(self, p):
        return self.WhitePlayer if p.color is "black" else self.BlackPlayer

def getFirstOccupiedSquareTowards(direction, piece, b):
    if direction is "l":
        dx = -1
        dy = 0
    elif direction is "lup":
        dx = -1
        dy = 1
    elif direction is "up":
        dx = 0
        dy = 1
    elif direction is "rup":
        dx = 1
        dy = 1
    elif direction is "r":
        dx = 1
        dy = 0
    elif direction is "rdwn":
        dx = 1
        dy = -1
    elif direction is "dwn":
        dx = 0
        dy = -1
    elif direction is "ldwn":
        dx = -1
        dy = -1
    else:
        return

    returnedPiece = None
    xoffset = dx
    yoffset = dy

    while(returnedPiece is None):
        s = b.getSquareAt(piece.square.xpos + xoffset, piece.square.ypos + yoffset)
        if s is None:
            return
        returnedPiece = s.occupyingPiece
        xoffset += dx
        yoffset += dy

    return returnedPiece
