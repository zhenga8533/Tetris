# Simple pygame program
import copy

# Import and initialize the pygame library
import pygame
from pygame import *
import block
from random import randint

# Start pygame
pygame.init()
pygame.font.init()

# Constants ------------------------------------------------------------------------------------------------------------
GAME_WIDTH = 10
GAME_HEIGHT = 20
TILE_SIZE = 30

GUI_WIDTH = 7

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 152, 146)

# Variables ------------------------------------------------------------------------------------------------------------

# Set up the drawing window
screen = pygame.display.set_mode(((GAME_WIDTH + GUI_WIDTH) * TILE_SIZE, GAME_HEIGHT * TILE_SIZE))

# Board
board = []

for r in range(GAME_HEIGHT):
    board.append([WHITE] * GAME_WIDTH)

# Global game variables
running = True
tick = 0
tick_speed = 1
action = [0, 1]
held = False

# User blocks
current_block = block.Block(randint(0, 6))
ghost_block = current_block.find_ghost(board)
held_block = block.Block(randint(0, 6))
next_block = block.Block(randint(0, 6))


# Functions ------------------------------------------------------------------------------------------------------------

# Draw Board
def draw_board():
    # White background
    screen.fill(WHITE)

    # Draw current_block block
    for b in current_block.pos:
        shape = pygame.Rect(b[0] * TILE_SIZE, b[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, current_block.color, shape)
        pygame.draw.rect(screen, BLACK, shape, 1)

    # Draw ghost block
    for b in ghost_block:
        shape = pygame.Rect(b[0] * TILE_SIZE, b[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, BLACK, shape, 1)

    # Draw board
    for y in range(GAME_HEIGHT):
        for x in range(GAME_WIDTH):
            if board[y][x] != WHITE:
                shape = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(screen, board[y][x], shape)
                pygame.draw.rect(screen, BLACK, shape, 1)

    # Draw GUI
    corbel = pygame.font.SysFont('Corbel', 40, True)

    # Frame
    shape = pygame.Rect(GAME_WIDTH * TILE_SIZE, 0, GUI_WIDTH * TILE_SIZE, GAME_HEIGHT * TILE_SIZE)
    pygame.draw.rect(screen, GRAY, shape)
    pygame.draw.rect(screen, BLACK, shape, 5)

    # Held Block
    shape = pygame.Rect((GAME_WIDTH + 1) * TILE_SIZE, 2 * TILE_SIZE, 5 * TILE_SIZE, 4 * TILE_SIZE)
    pygame.draw.rect(screen, BLACK, shape, 3)
    for b in held_block.pos:
        shape = pygame.Rect((b[0] + 8.5) * TILE_SIZE, (b[1] + 3) * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, held_block.color, shape)
        pygame.draw.rect(screen, BLACK, shape, 1)

    text = corbel.render('Hold', True, BLACK)
    text_rect = text.get_rect(center=((GAME_WIDTH + GUI_WIDTH / 2) * TILE_SIZE, 1.5 * TILE_SIZE))
    screen.blit(text, text_rect)

    # Next Block

    # Boarder and text
    shape = pygame.Rect((GAME_WIDTH + 1) * TILE_SIZE, 8 * TILE_SIZE, 5 * TILE_SIZE, 4 * TILE_SIZE)
    pygame.draw.rect(screen, BLACK, shape, 3)

    text = corbel.render('Next', True, BLACK)
    text_rect = text.get_rect(center=((GAME_WIDTH + GUI_WIDTH / 2) * TILE_SIZE, 7.5 * TILE_SIZE))
    screen.blit(text, text_rect)

    for b in next_block.pos:  # Draw from next block variables
        shape = pygame.Rect((b[0] + 8.5) * TILE_SIZE, (b[1] + 9) * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, next_block.color, shape)
        pygame.draw.rect(screen, BLACK, shape, 1)

    # Next Block

    # Update pygame display
    pygame.display.flip()


# Draw Board
def place_block():
    for xy in current_block.pos:
        board[xy[1]][xy[0]] = current_block.color

    # Check for filled lines
    clear_board()


# Clear board
def clear_board():
    clear_list = []
    line_fill = True

    # Detects what lines need to be cleared
    for y in range(GAME_HEIGHT):
        for x in range(GAME_WIDTH):
            if board[y][x] == WHITE:
                line_fill = False
        if line_fill:
            clear_list.append(y)
        line_fill = True

    # Clears the board
    for line in clear_list:
        del board[line]
        board.insert(0, [WHITE] * GAME_WIDTH)


# Run the game! --------------------------------------------------------------------------------------------------------

def run():
    # Starting game board
    global running, current_block, next_block, held, held_block, tick, ghost_block, event
    draw_board()
    pygame.display.update()

    while running:
        # Detect button presses
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Close game
                    running = False
                elif event.key == K_a:  # Move left
                    current_block.move([-1, 0], board)
                elif event.key == K_d:  # Move right
                    current_block.move([1, 0], board)
                elif event.key == K_w:  # Rotate block
                    current_block.rotate(90, board)
                elif event.key == K_s:  # Move down
                    if current_block.move([0, 1], board):
                        place_block()
                        current_block = next_block
                        next_block = block.Block(randint(0, 6))
                elif event.key == K_SPACE:
                    while not current_block.move([0, 1], board):
                        continue
                    place_block()
                    current_block = next_block
                    next_block = block.Block(randint(0, 6))
                elif event.key == K_c and not held:  # Change current block with held block
                    temp = copy.deepcopy(current_block)
                    current_block = held_block
                    held_block = block.Block(temp.shape)
                    held = True
                ghost_block = current_block.find_ghost(board)
                draw_board()
            elif event.type == pygame.QUIT:
                running = False

        if tick >= 1000000:
            if current_block.move([0, 1], board):
                place_block()
                current_block = next_block
                next_block = block.Block(randint(0, 6))
            ghost_block = current_block.find_ghost(board)
            draw_board()

            # Flip the display
            pygame.display.flip()
            tick = 0
        else:
            tick += tick_speed

    # Done! Time to quit.
    pygame.quit()


if __name__ == "__main__":
    run()
