# Maze Generator

import pygame
from constants import *
from functions import *

# Initialize
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator")
clock = pygame.time.Clock()

# Create variables that have the state of the maze
squares_side = WIDTH // SQUARE_SIZE         # Number of squares per side

# Each cell of the maze is composed by 4 letters (l)eft, (u)p, (d)own, (r)ight that identifies which walls they have
maze = [['lurd' for i in range(squares_side)] for j in range(squares_side)]

current = (0, 0)            # Maze starts being generated in top left corner


# Create lists that contain the cells that were already visited and the ones that were not
unvisited = [(i, j) for i in range(squares_side) for j in range(squares_side)]
unvisited.remove(current)

visited = [current]


finished = False

while not finished:
    # Set FPS
    clock.tick(FPS)


    # Listen to events
    for event in pygame.event.get():

        # In case red cross is clicked it closes the window
        if event.type == pygame.QUIT:
            finished = True
            pygame.quit()



    # Draw
    screen.fill(BGCOLOR)
    drawMaze(maze, screen, SQUARE_SIZE, current)


    #Logic
    maze, current, visited, unvisited = nextMove(current, maze, unvisited, visited)


    # Render
    pygame.display.flip()

# When the loop finished we close pygame
pygame.quit()


# ENJOY