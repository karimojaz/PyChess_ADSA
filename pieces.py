class piece:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

class pawn(piece):
    def __init__(self, xpos, ypos):
        piece.__init__(xpos, ypos)

class rook(piece):
    def __init__(self, xpos, ypos):
        piece.__init__(xpos, ypos)

class knight(piece):
    def __init__(self, xpos, ypos):
        piece.__init__(xpos, ypos)

class bishop(piece):
    def __init__(self, xpos, ypos):
        piece.__init__(xpos, ypos)

class queen(piece):
    def __init__(self, xpos, ypos):
        piece.__init__(xpos, ypos)

class king(piece):
    def __init__(self, xpos, ypos):
        piece.__init__(xpos, ypos)
