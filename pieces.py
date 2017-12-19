import pygame
import board
import moves

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
        elif self.owner.pieceSet.king.isInCheck():
            return
        capturedPiece = None
        if newSquare.occupyingPiece is not None and newSquare.occupyingPiece.owner.color is not self.owner.color:
            capturedPiece = newSquare.occupyingPiece
            capturedPiece.owner.pieceSet.erase(capturedPiece)
        oldSquare = self.square
        oldSquare.occupyingPiece = None
        self.square = newSquare
        self.square.occupyingPiece = self
        self.xpos = self.square.xpos
        self.ypos = self.square.ypos
        if self.owner.pieceSet.king.isInCheck():
            self.square.occupyingPiece = capturedPiece
            self.square = oldSquare
            self.square.occupyingPiece = self
            self.xpos = self.square.xpos
            self.ypos = self.square.ypos
            self.owner.b.switchPlayers()
            if capturedPiece is not None:
                if capturedPiece.owner.color is not self.owner.color:
                    self.owner.b.getOpponent(self.owner).pieceSet.add(capturedPiece)

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
                y = 1 if self.owner.color is "white" else -1
                if destSquare.ypos - fromSquare.ypos is y:
                    return True
                if abs(destSquare.ypos - fromSquare.ypos) is 2 and not self.hasMoved:
                    if self.owner.b.getSquareAt(fromSquare.xpos, fromSquare.ypos + y).occupyingPiece is None:
                        return True
        return False

    def controls(self, s):
        y = 1 if self.owner.color is "white" else -1
        return abs(self.square.xpos - s.xpos) is 1 and self.square.ypos + y is s.ypos

class Rook(Piece):

    def __init__(self, xpos, ypos, owner):
        Piece.__init__(self, xpos, ypos, owner)
        self.sprite = pygame.image.load("imgres/" + ("br.png" if (self.owner.color == "black") else "wr.png")).convert_alpha()

    def isMoveLegal(self, fromSquare, destSquare):
        if destSquare.occupyingPiece is self:
            return True
        if fromSquare.xpos is destSquare.xpos or fromSquare.ypos is destSquare.ypos:
            if fromSquare.xpos > destSquare.xpos:
                direction = "l"
            elif fromSquare.xpos < destSquare.xpos:
                direction = "r"
            elif fromSquare.ypos > destSquare.ypos:
                direction = "dwn"
            elif fromSquare.ypos < destSquare.ypos:
                direction = "up"
            else:
                return False
            p = board.getFirstOccupiedSquareTowards(direction, self, self.owner.b)
            if p is None:
                return True
            else:
                if p.owner.color is not self.owner.color and p.square is destSquare:
                    return True
                if p.square is not destSquare:
                    if direction is "l" and destSquare.xpos > p.square.xpos:
                        return True
                    if direction is "r" and destSquare.xpos < p.square.xpos:
                        return True
                    if direction is "up" and destSquare.ypos < p.square.ypos:
                        return True
                    if direction is "dwn" and destSquare.ypos > p.square.ypos:
                        return True
        return False

    def controls(self, s):
        if self.isMoveLegal(self.square, s) and s is not self.square:
            return True
        elif self.square.xpos is s.xpos or self.square.ypos is s.ypos:
            if self.square.xpos > s.xpos:
                direction = "l"
            elif self.square.xpos < s.xpos:
                direction = "r"
            elif self.square.ypos > s.ypos:
                direction = "dwn"
            elif self.square.ypos < s.ypos:
                direction = "up"
            else:
                return False
            p = board.getFirstOccupiedSquareTowards(direction, self, self.owner.b)
            if p.square is  s:
                return True
        return False

class Knight(Piece):

    def __init__(self, xpos, ypos, owner):
        Piece.__init__(self, xpos, ypos, owner)
        self.sprite = pygame.image.load("imgres/" + ("bn.png" if (self.owner.color == "black") else "wn.png")).convert_alpha()

    def isMoveLegal(self, fromSquare, destSquare):
        if destSquare is fromSquare:
            return True
        if (abs(destSquare.ypos - fromSquare.ypos) is 2 and abs(destSquare.xpos - fromSquare.xpos) is 1) or (abs(destSquare.ypos - fromSquare.ypos) is 1 and abs(destSquare.xpos - fromSquare.xpos) is 2):
            if (destSquare.occupyingPiece is None or destSquare.occupyingPiece.owner.color is not self.owner.color):
                return True
        return False

    def controls(self, s):
        if self.isMoveLegal(self.square, s) and s is not self.square:
            return True
        if (abs(s.ypos - self.square.ypos) is 2 and abs(s.xpos - self.square.xpos) is 1) or (abs(s.ypos - self.square.ypos) is 1 and abs(s.xpos - self.square.xpos) is 2):
            return True
        return False

class Bishop(Piece):

    def __init__(self, xpos, ypos, owner):
        Piece.__init__(self, xpos, ypos, owner)
        self.sprite = pygame.image.load("imgres/" + ("bb.png" if (self.owner.color == "black") else "wb.png")).convert_alpha()

    def isMoveLegal(self, fromSquare, destSquare):
        if destSquare.occupyingPiece is self:
            return True
        if (abs(destSquare.xpos - fromSquare.xpos) is abs(destSquare.ypos - fromSquare.ypos)):
            if fromSquare.xpos > destSquare.xpos and fromSquare.ypos > destSquare.ypos:
                direction = "ldwn"
            elif fromSquare.xpos > destSquare.xpos and fromSquare.ypos < destSquare.ypos:
                direction = "lup"
            elif fromSquare.xpos < destSquare.xpos and fromSquare.ypos > destSquare.ypos:
                direction = "rdwn"
            elif fromSquare.xpos < destSquare.xpos and fromSquare.ypos < destSquare.ypos:
                direction = "rup"
            else:
                return False
            p = board.getFirstOccupiedSquareTowards(direction, self, self.owner.b)
            if p is None:
                return True
            else:
                if p.owner.color is not self.owner.color and p.square is destSquare:
                    return True
                if p.square is not destSquare:
                    if direction is "ldwn" and destSquare.ypos > p.square.ypos and destSquare.xpos > p.square.xpos:
                        return True
                    if direction is "lup" and destSquare.ypos < p.square.ypos and destSquare.xpos > p.square.xpos:
                        return True
                    if direction is "rdwn" and destSquare.ypos > p.square.ypos and destSquare.xpos < p.square.xpos:
                        return True
                    if direction is "rup" and destSquare.ypos < p.square.ypos and destSquare.xpos < p.square.xpos:
                        return True
        return False

    def controls(self, s):
        if self.isMoveLegal(self.square, s) and s is not self.square:
            return True
        elif (abs(s.xpos - self.square.xpos) is abs(s.ypos - self.square.ypos)):
            if self.square.xpos > s.xpos and self.square.ypos > s.ypos:
                direction = "ldwn"
            elif self.square.xpos > s.xpos and self.square.ypos < s.ypos:
                direction = "lup"
            elif self.square.xpos < s.xpos and self.square.ypos > s.ypos:
                direction = "rdwn"
            elif self.square.xpos < s.xpos and self.square.ypos < s.ypos:
                direction = "rup"
            else:
                return False
            p = board.getFirstOccupiedSquareTowards(direction, self, self.owner.b)
            if p.square is  s:
                return True
        return False

class Queen(Piece):

    def __init__(self, xpos, ypos, owner):
        Piece.__init__(self, xpos, ypos, owner)
        self.sprite = pygame.image.load("imgres/" + ("bq.png" if (self.owner.color == "black") else "wq.png")).convert_alpha()

    def isMoveLegal(self, fromSquare, destSquare):
        if destSquare.occupyingPiece is self:
            return True
        p = -1
        direction = ""
        if abs(destSquare.xpos - fromSquare.xpos) is abs(destSquare.ypos - fromSquare.ypos):
            if fromSquare.xpos > destSquare.xpos and fromSquare.ypos > destSquare.ypos:
                direction = "ldwn"
            elif fromSquare.xpos > destSquare.xpos and fromSquare.ypos < destSquare.ypos:
                direction = "lup"
            elif fromSquare.xpos < destSquare.xpos and fromSquare.ypos > destSquare.ypos:
                direction = "rdwn"
            elif fromSquare.xpos < destSquare.xpos and fromSquare.ypos < destSquare.ypos:
                direction = "rup"
            p = board.getFirstOccupiedSquareTowards(direction, self, self.owner.b)
        elif fromSquare.xpos is destSquare.xpos or fromSquare.ypos is destSquare.ypos:
            if fromSquare.xpos > destSquare.xpos:
                direction = "l"
            elif fromSquare.xpos < destSquare.xpos:
                direction = "r"
            elif fromSquare.ypos > destSquare.ypos:
                direction = "dwn"
            elif fromSquare.ypos < destSquare.ypos:
                direction = "up"
            p = board.getFirstOccupiedSquareTowards(direction, self, self.owner.b)
        if p is None:
            return True
        elif p is -1:
            return False
        else:
            if p.owner.color is not self.owner.color and p.square is destSquare:
                return True
            if p.square is not destSquare:
                if direction is "ldwn" and destSquare.ypos > p.square.ypos and destSquare.xpos > p.square.xpos:
                    return True
                if direction is "lup" and destSquare.ypos < p.square.ypos and destSquare.xpos > p.square.xpos:
                    return True
                if direction is "rdwn" and destSquare.ypos > p.square.ypos and destSquare.xpos < p.square.xpos:
                    return True
                if direction is "rup" and destSquare.ypos < p.square.ypos and destSquare.xpos < p.square.xpos:
                    return True
                if direction is "l" and destSquare.xpos > p.square.xpos:
                    return True
                if direction is "r" and destSquare.xpos < p.square.xpos:
                    return True
                if direction is "up" and destSquare.ypos < p.square.ypos:
                    return True
                if direction is "dwn" and destSquare.ypos > p.square.ypos:
                    return True
        return False

    def controls(self, s):
        return self.isMoveLegal(self.square, s)

class King(Piece):

    def __init__(self, xpos, ypos, owner):
        Piece.__init__(self, xpos, ypos, owner)
        self.sprite = pygame.image.load("imgres/" + ("bk.png" if (self.owner.color == "black") else "wk.png")).convert_alpha()

    def isMoveLegal(self, fromSquare, destSquare):
        if destSquare.occupyingPiece is self:
            return True
        if abs(destSquare.xpos - fromSquare.xpos) < 2 and abs(destSquare.ypos - fromSquare.ypos) < 2 and (destSquare.isFree() or destSquare.occupyingPiece.owner.color is not self.owner.color):
            return True
        return False

    def controls(self, s):
        return self.isMoveLegal(self.square, s)

    def isInCheck(self):
        return self.square in self.owner.b.getOpponent(self.owner).getControlledSquares()
