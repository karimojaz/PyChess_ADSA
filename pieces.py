import pygame
import board

class Piece:

    def __init__(self, xpos, ypos, owner):
        self.xpos = xpos
        self.ypos = ypos
        self.square = board.Square(xpos, ypos)
        self.owner = owner
        self.sprite = None
        self.hasMoved = False

    def moveTo(self, newSquare):
        if newSquare is not self.square:
            self.hasMoved = True
        self.square.occupyingPiece = None
        self.square = newSquare
        self.square.occupyingPiece = self
        self.xpos = self.square.xpos
        self.ypos = self.square.ypos

    def checkBasicLegality(self, destSquare):
        if destSquare.isFree():
            return True
        elif destSquare.occupyingPiece is self:
            return True
        else:
            return False

class Pawn(Piece):

    def __init__(self, xpos, ypos, owner):
        Piece.__init__(self, xpos, ypos, owner)
        self.sprite = pygame.image.load("imgres/" + ("bp.png" if (self.owner.color == "black") else "wp.png")).convert_alpha()

    def isMoveLegal(self, fromSquare, destSquare):
        if destSquare.occupyingPiece is self:
            return True
        if not destSquare.isFree():
            if destSquare.occupyingPiece.owner.color is not self.owner.color and abs(destSquare.xpos - fromSquare.xpos) is 1 and destSquare.ypos is ((fromSquare.ypos + 1) if self.owner.color is "white" else (fromSquare.ypos - 1)):
                return True
        else:
            if(destSquare.xpos is fromSquare.xpos):
                if abs(destSquare.ypos - fromSquare.ypos) is 1:
                    return True
                if abs(destSquare.ypos - fromSquare.ypos) is 2 and not self.hasMoved:
                    return True
        return False

class Rook(Piece):

    def __init__(self, xpos, ypos, owner):
        Piece.__init__(self, xpos, ypos, owner)
        self.sprite = pygame.image.load("imgres/" + ("br.png" if (self.owner.color == "black") else "wr.png")).convert_alpha()

class Knight(Piece):

    def __init__(self, xpos, ypos, owner):
        Piece.__init__(self, xpos, ypos, owner)
        self.sprite = pygame.image.load("imgres/" + ("bn.png" if (self.owner.color == "black") else "wn.png")).convert_alpha()

class Bishop(Piece):

    def __init__(self, xpos, ypos, owner):
        Piece.__init__(self, xpos, ypos, owner)
        self.sprite = pygame.image.load("imgres/" + ("bb.png" if (self.owner.color == "black") else "wb.png")).convert_alpha()

class Queen(Piece):

    def __init__(self, xpos, ypos, owner):
        Piece.__init__(self, xpos, ypos, owner)
        self.sprite = pygame.image.load("imgres/" + ("bq.png" if (self.owner.color == "black") else "wq.png")).convert_alpha()

class King(Piece):

    def __init__(self, xpos, ypos, owner):
        Piece.__init__(self, xpos, ypos, owner)
        self.sprite = pygame.image.load("imgres/" + ("bk.png" if (self.owner.color == "black") else "wk.png")).convert_alpha()
