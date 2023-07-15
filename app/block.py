import copy
import math

# Color Constants
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 69, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Block(object):
    def __init__(self, shape):
        if shape == 'I' or shape == 0:
            self.center = [4.5, 0.5]
            self.pos = [[3, 0], [4, 0], [5, 0], [6, 0]]
            self.color = CYAN
        elif shape == 'J' or shape == 1:
            self.center = [5, 0]
            self.pos = [[4, 0], [5, 0], [6, 0], [6, 1]]
            self.color = BLUE
        elif shape == 'L' or shape == 2:
            self.center = [4, 0]
            self.pos = [[3, 1], [3, 0], [4, 0], [5, 0]]
            self.color = ORANGE
        elif shape == 'O' or shape == 3:
            self.center = [4.5, 0.5]
            self.pos = [[4, 0], [4, 1], [5, 1], [5, 0]]
            self.color = YELLOW
        elif shape == 'S' or shape == 4:
            self.center = [5, 1]
            self.pos = [[4, 1], [5, 1], [5, 0], [6, 0]]
            self.color = GREEN
        elif shape == 'T' or shape == 5:
            self.center = [4, 0]
            self.pos = [[3, 0], [4, 0], [5, 0], [4, 1]]
            self.color = PURPLE
        else:
            self.center = [4, 1]
            self.pos = [[3, 0], [4, 0], [4, 1], [5, 1]]
            self.color = RED

    def rotate(self, angle, board):
        for i in range(len(self.pos)):
            x = (self.pos[i][0] - self.center[0]) * math.sin(math.radians(angle))
            y = (self.pos[i][1] - self.center[1]) * math.sin(math.radians(angle))

            self.pos[i][0] = round(-y + self.center[0])
            self.pos[i][1] = round(x + self.center[1])

        if self.detect_hit(board):
            self.rotate(-angle, board)

    def move(self, change, board):
        for p in self.pos:
            p[0] += change[0]
            p[1] += change[1]

        self.center[0] += change[0]
        self.center[1] += change[1]

        if self.detect_hit(board):
            self.move([-change[0], -change[1]], board)
            return True

        return False

    def find_ghost(self, board):
        ghost = copy.deepcopy(self)
        while not ghost.move([0, 1], board):
            continue
        return ghost.pos

    def detect_hit(self, board):
        for p in self.pos:
            if p[1] == len(board):  # Check ground
                return True
            elif not (0 <= p[0] < len(board[0])):  # Check side
                return True
            elif board[p[1]][p[0]] != WHITE:  # Check board
                return True

        return False
