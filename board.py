import pieces

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

class Player:

    def __init__(self, color):
        self.color = color
        self.pieceSet = PieceSet(self)

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

    def getPieces(self):
        return self.pawns + self.bishops + self.knights + self.rooks + [self.queen, self.king]

class Board:

    def __init__(self):
        self.WhitePlayer = Player("white")
        self.BlackPlayer = Player("black")
        self.squares = []

        for x in range(8):
            for y in range(8):
                self.squares.append(Square(x, y))

        for p in self.WhitePlayer.pieceSet.getPieces():
            self.getSquareAt(p.xpos, p.ypos).occupyingPiece = p
            p.square = self.getSquareAt(p.xpos, p.ypos)

        for p in self.BlackPlayer.pieceSet.getPieces():
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
