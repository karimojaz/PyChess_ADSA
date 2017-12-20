import board
import pieces
import moves
import random

class Node:

    def __init__(self, payload):
        self.payload = payload
        self.children = []

    def append(self, n):
        self.children.append(n)

class Tree:

    def __init__(self, root):
        self.root = root

class BasicAI:

    def __init__(self, position):
        self.position = position

    def evaluate(self):
        self.position.computePossibleMoves()
        m = self.position.legalMoves[random.randint(0, len(self.position.legalMoves) - 1)]
        m.piece.moveTo(m.destSquare)
