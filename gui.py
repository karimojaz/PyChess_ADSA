import pygame
import moves
import tkinter
from tkinter import messagebox

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
    if convertToCoord(piece.xpos, piece.ypos)[0] >= CONST_BOARD_OFFSET and convertToCoord(piece.xpos, piece.ypos)[1] >= CONST_BOARD_OFFSET:
        window.blit(piece.sprite, convertToCoord(piece.xpos, piece.ypos))

def convertToCoord(xpos, ypos):
    return (CONST_SQUARE_DIM * xpos + CONST_BOARD_OFFSET, CONST_SQUARE_DIM * (7-ypos) + CONST_BOARD_OFFSET)

def convertFromCoord(coord):
    return ((coord - CONST_BOARD_OFFSET) - (coord % CONST_SQUARE_DIM)) // CONST_SQUARE_DIM

def displayPiecesOfBoard(window, board):
    for s in board.squares:
        if(s.occupyingPiece and s.occupyingPiece.owner.color is not board.currentPlayer.color):
            putSprite(window, s.occupyingPiece)
    for s in board.squares:
        if(s.occupyingPiece and s.occupyingPiece.owner.color is board.currentPlayer.color):
            putSprite(window, s.occupyingPiece)
    pygame.display.flip()

def flushBoard(window, board):
    window.blit(pygame.image.load("imgres/board.jpg").convert(), (CONST_BOARD_OFFSET, CONST_BOARD_OFFSET))
    displayPiecesOfBoard(window, board)
    print(board)
    i = 0
    for m in moves.Position(board.currentPlayer, board.squares).computePossibleMoves():
        print(m)
        i+=1
    print(str(i) + " possible moves computed")

    if len(moves.Position(board.WhitePlayer, board.squares).computePossibleMoves()) == 0:
        if board.WhitePlayer.pieceSet.king.isInCheck():
            print("WHITE MATED")
        else:
            print("PAT")
    elif board.WhitePlayer.pieceSet.king.isInCheck():
        print("WHITE CHECKED")

    if len(moves.Position(board.BlackPlayer, board.squares).computePossibleMoves()) == 0:
        if board.BlackPlayer.pieceSet.king.isInCheck():
            print("BLACK MATED")
        else:
            print("PAT")
    elif board.BlackPlayer.pieceSet.king.isInCheck():
        print("BLACK CHECKED")

def clickIsOnTheChessboard(event):
    return (event.pos[0] > CONST_BOARD_OFFSET and event.pos[0] <= (CONST_BOARD_OFFSET + 8 * CONST_SQUARE_DIM) and event.pos[1] > CONST_BOARD_OFFSET and event.pos[1] <= (CONST_BOARD_OFFSET + 8 * CONST_SQUARE_DIM))

def grabAPiece(xpos, ypos, board):
    if board.getSquareAt(convertFromCoord(xpos), 7 - convertFromCoord(ypos)) is not None:
        return board.getSquareAt(convertFromCoord(xpos), 7 - convertFromCoord(ypos)).occupyingPiece
