class Piece:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

class Pawn(Piece):
    def __init__(self, xpos, ypos):
        Piece.__init__(xpos, ypos)

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
