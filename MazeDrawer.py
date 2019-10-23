import sys, pygame
from Maze import Maze

def Draw(windowSize, width, height, delayBetweenSteps):
    maze = Maze(width, height)

    pygame.init()
    ratioX = len(maze.nodes)
    ratioY = len(maze.nodes[0])
    highest = ratioX if ratioX > ratioY else ratioY
    ratioX /= highest
    ratioY /= highest

    size = width, height = round(windowSize*ratioX), round(windowSize*ratioY)
    blockSize = width / len(maze.nodes)

    screen = pygame.display.set_mode(size)

    white = 45,141,175
    screen.fill(white)

    while 1:
        node, done = maze.generateNextStep()
        if node == None:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_SPACE:
                        white = 45,141,175
                        screen.fill(white)
                        maze = Maze(width, height)
                        pygame.display.update()
                        continue
            continue

        pygame.time.delay(delayBetweenSteps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE:
                    white = 45,141,175
                    screen.fill(white)
                    maze = Maze(width, height)
                    pygame.display.update()
                    continue

        if len(maze.nodeStack) != 0:
            pygame.draw.rect(screen, (202, 250, 140), (maze.currentNode.x*blockSize, maze.currentNode.y * blockSize, blockSize+2*ratioY, blockSize+2*ratioX))
        else:
            pygame.draw.rect(screen, (94,225,167), (maze.currentNode.x*blockSize, maze.currentNode.y * blockSize, blockSize+2*ratioY, blockSize+2*ratioX))
            drawWalls(maze.currentNode.x, maze, maze.currentNode.y, screen, blockSize, ratioY, ratioX)

        if done == True:
            pygame.draw.rect(screen, (94,225,167), (node.x*blockSize, node.y * blockSize, blockSize+2*ratioY, blockSize+2*ratioX))
        else:
            pygame.draw.rect(screen, (226,166,94), (node.x*blockSize, node.y * blockSize, blockSize+2*ratioY, blockSize+2*ratioX))

        x = node.x
        y = node.y
        drawWalls(x, maze, y, screen, blockSize, ratioY, ratioX)

        if maze.nodes[x][y].visited == False:
            pygame.draw.rect(screen, (45,141,175), (x*blockSize, y * blockSize, blockSize+2*ratioY, blockSize+2*ratioX))

        pygame.display.update()

def drawWalls(x, maze, y, screen, blockSize, ratioY, ratioX):
    if x+1 < len(maze.nodes) and maze.nodes[x+1][y].nodes.count(maze.nodes[x][y]) == 0 and maze.nodes[x][y].visited == True and maze.nodes[x+1][y].visited == True:
        pygame.draw.rect(screen, (0,0,0), ((x+1)*blockSize, y*blockSize, 2*ratioY, blockSize+2*ratioX))
    if x > 0 and maze.nodes[x-1][y].nodes.count(maze.nodes[x][y]) == 0 and maze.nodes[x][y].visited == True and maze.nodes[x-1][y].visited == True:
        pygame.draw.rect(screen, (0,0,0), ((x)*blockSize, y*blockSize, 2*ratioY, blockSize+2*ratioX))
    if y+1 < len(maze.nodes[x]) and maze.nodes[x][y+1].nodes.count(maze.nodes[x][y]) == 0 and maze.nodes[x][y].visited == True and maze.nodes[x][y+1].visited == True:
        pygame.draw.rect(screen, (0,0,0), (x*blockSize, (y+1)*blockSize, blockSize+2*ratioY, 2*ratioX))
    if y > 0 and maze.nodes[x][y-1].nodes.count(maze.nodes[x][y]) == 0 and maze.nodes[x][y].visited == True  and maze.nodes[x][y-1].visited == True:
        pygame.draw.rect(screen, (0,0,0), (x*blockSize, (y)*blockSize, blockSize+2*ratioY, 2*ratioX))

