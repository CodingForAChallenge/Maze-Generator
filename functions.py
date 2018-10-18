import pygame
import random

def drawMaze(maze, surface, square_size, current):

    # Draw the position of current in the maze in green
    pygame.draw.rect(surface,
            (0, 255, 0), 
            (current[1] * square_size,
            current[0] * square_size,
            square_size,
            square_size),    
        )
    
    for i, line in enumerate(maze):
        for j, element in enumerate(line):
            
            # If 'l' is contained in the string of the element it means it still has the left wall, so we draw it
            if 'l' in element:
                pygame.draw.line(surface,
                    (0 , 0, 0),                                         # Color
                    (j * square_size, i * square_size),                 # Starting position of line
                    (j * square_size, i * square_size + square_size),   # Ending position ofline
                    2                                                   # Thickness of line
                )

            # If 'u' is contained in the string of the element it means it still has the up wall, so we draw it
            if 'u' in element:
                pygame.draw.line(surface,
                    (0 , 0, 0),
                    (j * square_size, i * square_size),
                    (j * square_size + square_size, i * square_size),
                    2
                )

            # If 'r' is contained in the string of the element it means it still has the right wall, so we draw it
            if 'r' in element:
                pygame.draw.line(surface,
                    (0 , 0, 0),
                    (j * square_size + square_size, i * square_size),
                    (j * square_size + square_size, i * square_size + square_size),
                    2
                )

            # If 'd' is contained in the string of the element it means it still has the down wall, so we draw it
            if 'd' in element:
                pygame.draw.line(surface,
                    (0 , 0, 0),
                    (j * square_size, i * square_size + square_size),
                    (j * square_size + square_size, i * square_size + square_size),
                    2
                )

def nextMove(current, maze, unvisited, visited):

    # Define list that contains all the possible movements of the current cell
    neighbours = []

    # If the next line is in unvisited and does not exceed the length of the maze it is a possibility to move there
    if current[0] + 1 < len(maze) and (current[0] + 1, current[1]) in unvisited:
        neighbours.append((current[0] + 1, current[1]))

    # If the next column is in unvisited and does not exceed the length of the maze it is a possibility to move there
    if current[1] + 1 < len(maze) and (current[0], current[1] + 1) in unvisited:
        neighbours.append((current[0], current[1] + 1))

    # If the previous line is in unvisited and does not exceed the length of the maze it is a possibility to move there
    if current[0] - 1 >= 0 and (current[0] - 1, current[1]) in unvisited:
        neighbours.append((current[0] - 1, current[1]))

    # If the previous column is in unvisited and does not exceed the length of the maze it is a possibility to move there
    if current[1] - 1 >= 0 and (current[0], current[1] - 1) in unvisited:
        neighbours.append((current[0], current[1] - 1))


    # If there is at least one possible movement
    if len(neighbours) > 0:

        # We choose a element randomly
        nextPos = random.choice(neighbours)

        # Now we need to now where to move
        if current[0] == nextPos[0]:            # Means it is in the same line
            if nextPos[1] > current[1]:         # Means we go right
                direction = 'r'
                maze[current[0]][current[1]] = maze[current[0]][current[1]].replace('r', '')    # Remove right wall of current
                maze[nextPos[0]][nextPos[1]] = maze[nextPos[0]][nextPos[1]].replace('l', '')    # Remove left wall of nextPos 

            else:                               # Means we go left
                direction = 'l'
                maze[current[0]][current[1]] = maze[current[0]][current[1]].replace('l', '')    # Remove left wall of current
                maze[nextPos[0]][nextPos[1]] = maze[nextPos[0]][nextPos[1]].replace('r', '')    # Remove righ wall of nextPos

        else:                                   # Means it is in the same column
            if nextPos[0] > current[0]:         # Means we go down
                direction = 'd'
                maze[current[0]][current[1]] = maze[current[0]][current[1]].replace('d', '')    # Remove down wall of current
                maze[nextPos[0]][nextPos[1]] = maze[nextPos[0]][nextPos[1]].replace('u', '')    # Remove up wall of nextPos 

            else:                               # Means we go up
                direction = 'u'
                maze[current[0]][current[1]] = maze[current[0]][current[1]].replace('u', '')    # Remove up wall of current
                maze[nextPos[0]][nextPos[1]] = maze[nextPos[0]][nextPos[1]].replace('d', '')    # Remove down wall of nextPos

    
        # Update position of current and add it to visited and remove it from unvisited
        current = nextPos
        if current not in visited:
            visited.append(current)

        if current in unvisited:
            unvisited.remove(current)
    
    # If there are no possible movements
    else:
        # If we are not in the initial situaltion of only (0, 0) in visited
        if len(visited) > 1:
            visited = visited[:-1]      # We remove the last element to go one step back since we are in a dead end
            current = visited[-1]       # We update current to be the new last element

        else:
            current = (0, 0)


    return maze, current, visited, unvisited