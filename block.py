import copy
import math


class Block(object):
    CYAN = (0, 255, 255)
    BLUE = (0, 0, 255)
    ORANGE = (255, 69, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    PURPLE = (128, 0, 128)
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self, shape):
        if shape == 'I' or shape == 0:
            self.center = [4.5, 0.5]
            self.pos = [[3, 0], [4, 0], [5, 0], [6, 0]]
            self.color = self.CYAN
        elif shape == 'J' or shape == 1:
            self.center = [5, 0]
            self.pos = [[4, 0], [5, 0], [6, 0], [6, 1]]
            self.color = self.BLUE
        elif shape == 'L' or shape == 2:
            self.center = [4, 0]
            self.pos = [[3, 1], [3, 0], [4, 0], [5, 0]]
            self.color = self.ORANGE
        elif shape == 'O' or shape == 3:
            self.center = [4.5, 0.5]
            self.pos = [[4, 0], [4, 1], [5, 1], [5, 0]]
            self.color = self.YELLOW
        elif shape == 'S' or shape == 4:
            self.center = [5, 1]
            self.pos = [[4, 1], [5, 1], [5, 0], [6, 0]]
            self.color = self.GREEN
        elif shape == 'T' or shape == 5:
            self.center = [4, 0]
            self.pos = [[3, 0], [4, 0], [5, 0], [4, 1]]
            self.color = self.PURPLE
        elif shape == 'Z' or shape == 6:
            self.center = [4, 1]
            self.pos = [[3, 0], [4, 0], [4, 1], [5, 1]]
            self.color = self.RED
        self.shape = shape

    def rotate(self, angle, board):
        for i in range(len(self.pos)):
            x = (self.pos[i][0] - self.center[0]) * math.sin(math.radians(angle))
            y = (self.pos[i][1] - self.center[1]) * math.sin(math.radians(angle))

            self.pos[i][0] = round(-y + self.center[0])
            self.pos[i][1] = round(x + self.center[1])

        if self.detect_hit(board):
            self.rotate(-angle, board)

    def move(self, change, board):
        replace = False

        for p in self.pos:
            p[0] += change[0]
            p[1] += change[1]

        self.center[0] += change[0]
        self.center[1] += change[1]

        if self.detect_hit(board):
            self.move([change[0] * -1, change[1] * -1], board)
            replace = True

        return replace

    def find_ghost(self, board):
        ghost = copy.deepcopy(self)
        while not ghost.move([0, 1], board):
            continue
        return ghost.pos

    def detect_hit(self, board):
        hit = False

        for piece in self.pos:
            if piece[1] == len(board):  # Check ground
                hit = True
            elif not (0 <= piece[0] < len(board[0])):
                hit = True
            elif board[piece[1]][piece[0]] != self.WHITE:
                hit = True

        return hit
