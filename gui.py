import pygame

CONST_BOARD_OFFSET = 68
CONST_SQUARE_DIM = 82

def initializeUI():
    pygame.init()
    window = pygame.display.set_mode((1408, 792))
    pygame.display.set_caption('PyChess_ADSA')

    window.blit(pygame.image.load("imgres/bg.jpg").convert(), (0,0))
    window.blit(pygame.image.load("imgres/board.jpg").convert(), (CONST_BOARD_OFFSET, CONST_BOARD_OFFSET))
    pygame.display.flip()

    return window

def putSprite(window, piece):
    window.blit(piece.sprite, convertToCoord(piece.xpos, piece.ypos))

def convertToCoord(xpos, ypos):
    return (CONST_SQUARE_DIM * xpos + CONST_BOARD_OFFSET, CONST_SQUARE_DIM * (7-ypos) + CONST_BOARD_OFFSET)

def convertFromCoord(coord):
    return int((coord - (coord % CONST_SQUARE_DIM)) / CONST_SQUARE_DIM) - 1
#REGLE CA GROS FDP

def displayPiecesOfBoard(window, board):
    for s in board.squares:
        if(s.occupyingPiece):
            putSprite(window, s.occupyingPiece)
    pygame.display.flip()

def flushBoard(window, board):
    window.blit(pygame.image.load("imgres/board.jpg").convert(), (CONST_BOARD_OFFSET, CONST_BOARD_OFFSET))
    displayPiecesOfBoard(window, board)

def clickIsOnTheChessboard(event):
    return (event.pos[0] >= CONST_BOARD_OFFSET and event.pos[0] <= (CONST_BOARD_OFFSET + 8 * CONST_SQUARE_DIM) and event.pos[1] >= CONST_BOARD_OFFSET and event.pos[1] <= (CONST_BOARD_OFFSET + 8 * CONST_SQUARE_DIM))

def grabAPiece(xpos, ypos, board):
    return board.getSquareAt(convertFromCoord(xpos), 7 - convertFromCoord(ypos)).occupyingPiece
