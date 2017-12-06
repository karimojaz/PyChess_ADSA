import pygame

CONST_BOARD_OFFSET = 68
CONST_SQUARE_DIM = 82

def initializeUI():
    pygame.init()
    window = pygame.display.set_mode((1408, 792))
    pygame.display.set_caption('PyChess_ADSA')

    bg = pygame.image.load("imgres/bg.jpg").convert()
    window.blit(bg, (0,0))
    board = pygame.image.load("imgres/board.jpg").convert()
    window.blit(board, (CONST_BOARD_OFFSET, CONST_BOARD_OFFSET))
    pygame.display.flip()

    return window

def putSprite(window, piece):
    window.blit(piece.sprite, convertToCoord(piece.xpos, piece.ypos))

def convertToCoord(xpos, ypos):
    return (CONST_SQUARE_DIM * xpos + CONST_BOARD_OFFSET, CONST_SQUARE_DIM * (7-ypos) + CONST_BOARD_OFFSET)

def displayPiecesOfBoard(window, board):
    for s in board.squares:
        if(s.occupyingPiece):
            putSprite(window, s.occupyingPiece)
    pygame.display.flip()
