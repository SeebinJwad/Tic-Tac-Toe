import pygame
import time
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

pygame.init()

displayWidth = 600
displayHeight = 600

blue = (0, 0, 180)
red = (180, 0, 0)
light_blue = (225, 255, 255)
white = (255, 255, 255)
black = (0, 0, 0)

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Tic-Tac-Toe")

"""board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def move(turn, position, tic_board):
    tic_board[int(position) - 1] = turn


def print_board(tic_board):
    print(str(tic_board[0:3]) + "\n" + str(tic_board[3:6]) + "\n" + str(tic_board[6:9]))


# tb means tic-tac-toe board
# if position has x, add 1 so one row having x is 3; easier to check

# pc means position check
def pc(pos):
    if board[pos - 1] == "x":
        return 1
    if board[pos - 1] == "o":
        return -1
    else:
        return 0



def check():
    if pc(1) + pc(2) + pc(3) == 3 or \
            pc(4) + pc(5) + pc(6) == 3 or \
            pc(7) + pc(8) + pc(9) == 3 or \
            pc(1) + pc(4) + pc(7) == 3 or \
            pc(2) + pc(5) + pc(8) == 3 or \
            pc(3) + pc(6) + pc(9) == 3 or \
            pc(1) + pc(5) + pc(9) == 3 or \
            pc(3) + pc(5) + pc(7) == 3:
        print("X wins")
        quit()
    if pc(1) + pc(2) + pc(3) == -3 or \
            pc(4) + pc(5) + pc(6) == -3 or \
            pc(7) + pc(8) + pc(9) == -3 or \
            pc(1) + pc(4) + pc(7) == -3 or \
            pc(2) + pc(5) + pc(8) == -3 or \
            pc(3) + pc(6) + pc(9) == -3 or \
            pc(1) + pc(5) + pc(9) == -3 or \
            pc3) + pc(5) + pc(7) == -3:
        print("O wins")
        quit()
"""


def drawBoard():
    # board background
    # pygame.draw.rect(gameDisplay, white, [75, 75, 450, 450])
    # left vertical
    pygame.draw.rect(gameDisplay, black, [75 + 140, 75, 15, 450])
    # right vertical
    pygame.draw.rect(gameDisplay, black, [displayWidth - (75 + 140 + 15), 75, 15, 450])
    # top horizontal
    pygame.draw.rect(gameDisplay, black, [75, 75 + 140, 450, 15])
    # bottom horizontal
    pygame.draw.rect(gameDisplay, black, [75, displayHeight - (75 + 140 + 15), 450, 15])


def pos_check(board, pos):
    if board[pos - 1] == "X":
        return 1
    if board[pos - 1] == "O":
        return -1
    else:
        return 0


def check(board):
    if pos_check(board, 1) + pos_check(board, 2) + pos_check(board, 3) == 3 or \
            pos_check(board, 4) + pos_check(board, 5) + pos_check(board, 6) == 3 or \
            pos_check(board, 7) + pos_check(board, 8) + pos_check(board, 9) == 3 or \
            pos_check(board, 1) + pos_check(board, 4) + pos_check(board, 7) == 3 or \
            pos_check(board, 2) + pos_check(board, 5) + pos_check(board, 8) == 3 or \
            pos_check(board, 3) + pos_check(board, 6) + pos_check(board, 9) == 3 or \
            pos_check(board, 1) + pos_check(board, 5) + pos_check(board, 9) == 3 or \
            pos_check(board, 3) + pos_check(board, 5) + pos_check(board, 7) == 3:
        print("X wins")
        time.sleep(1)
        quit()
    if pos_check(board, 1) + pos_check(board, 2) + pos_check(board, 3) == -3 or \
            pos_check(board, 4) + pos_check(board, 5) + pos_check(board, 6) == -3 or \
            pos_check(board, 7) + pos_check(board, 8) + pos_check(board, 9) == -3 or \
            pos_check(board, 1) + pos_check(board, 4) + pos_check(board, 7) == -3 or \
            pos_check(board, 2) + pos_check(board, 5) + pos_check(board, 8) == -3 or \
            pos_check(board, 3) + pos_check(board, 6) + pos_check(board, 9) == -3 or \
            pos_check(board, 1) + pos_check(board, 5) + pos_check(board, 9) == -3 or \
            pos_check(board, 3) + pos_check(board, 5) + pos_check(board, 7) == -3:
        print("O wins")
        time.sleep(1)
        quit()

"""
def draw(d_pos, xo):
    if xo == "O":
        pygame.draw.rect(gameDisplay, black, [d_pos[0] - 50, d_pos[1] - 50, 50, 50])
        pygame.display.update()
"""


def gameLoop():
    gameOver = False
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    piece = "X"
    total_pos = []
    color_pos = white

    x1 = 75 + (140 / 2) - 25
    x2 = 75 + (140 / 2) + 15 + 140 - 25
    x3 = 75 + (140 / 2) + 15 + 140 + 155 - 25

    y1, y2, y3 = x1, x2, x3

    boardPosToCoordX = {1: x1, 2: x2, 3: x3,
                        4: x1, 5: x2, 6: x3,
                        7: x1, 8: x2, 9: x3}

    boardPosToCoordY = {1: y1, 2: y1, 3: y1,
                        4: y2, 5: y2, 6: y2,
                        7: y3, 8: y3, 9: y3}

    color_pos = {1: red, 2: blue, 3: red, 4: blue, 5: red, 6: blue, 7: red, 8: blue, 9: red}
    while not gameOver:
        move = " "
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True

            # moves

            pos = pygame.mouse.get_pos()
            # print(pos)

            pressed = pygame.mouse.get_pressed()
            # print(pressed)

            if pressed == (1, 0, 0):
                if pos[1] <= 215:
                    if pos[0] <= 215:
                        # print("A1")
                        move = "A1"
                    elif 230 <= pos[0] <= 370:
                        # print("A2")
                        move = "A2"
                    elif pos[0] >= 385:
                        # print("A3")
                        move = "A3"
                if 385 >= pos[1] >= 230:
                    if pos[0] <= 215:
                        # print("B1")
                        move = "B1"
                    elif 230 <= pos[0] <= 370:
                        # print("B2")
                        move = "B2"
                    elif pos[0] >= 385:
                        # print("B3")
                        move = "B3"
                if pos[1] >= 390:
                    if pos[0] <= 215:
                        # print("C1")
                        move = "C1"
                    elif 230 <= pos[0] <= 370:
                        # print("C2")
                        move = "C2"
                    elif pos[0] >= 385:
                        # print("C3")
                        move = "C3"

        row2num = {"A": 0, "B": 3, "C": 6}
        gameDisplay.fill(light_blue)
        board_pos = 0
        if move != " ":
            # dict board[1] = (75 + 140/2, 75 + 140/2) for each pos and run draw(board.get(pos), piece)
            board_pos = (int(move[1]) + row2num.get(str(move[0]))) - 1
            # total positions append this board pos

            # print(board_pos)
            if board[board_pos] == " ":
                total_pos.append(board_pos)
                if piece == "X":
                    board[board_pos] = piece
                    # print(board)
                    piece = "O"
                else:
                    board[board_pos] = piece
                    # print(board)
                    piece = "X"
        # count = 0 for each addition to count reference that part of the drawing
        for x in total_pos:
            if (total_pos.index(x) + 1) % 2 == 1:
                color_pos = red
            else:
                color_pos = blue
            # print(total_pos)
            pygame.draw.rect(gameDisplay, color_pos,
                             [boardPosToCoordX.get(x + 1), boardPosToCoordY.get(x + 1), 50, 50])

        drawBoard()
        check(board)
        if " " not in board:
            for x in range(15):
                print("TIE")
            quit()
        # create a for loop for each pos in board and draw it
        # for a in board, if a = x pygame.draw.rect (display, black, [draw_x.get(1), draw_y.get(1), 50, 50])
        pygame.display.update()
    pygame.quit()
    quit()
    """ 
        for x in range(9):

        if (x + 1) % 2 == 0:
            pos = input("O, what is your position: ")
            move("o", pos, board)

        else:
            pos = input("X, what is your position: ")
            move("x", pos, board)

        print_board(board)
        check()
    """


gameLoop()
