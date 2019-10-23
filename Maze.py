import random as rnd

class Maze():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.nodes = []
        for x in range(0, width):
            yRow = []
            for y in range(0, height):
                yRow.append(Node(x,y))
            self.nodes.append(yRow)

        self.startX = rnd.randint(0, self.width-1)
        self.startY = rnd.randint(0, self.height-1)

        self.currentNode = self.nodes[self.startX][self.startY]
        self.nodeStack = []
        self.started = False

    def generate(self):
        while self.started == False or len(self.nodeStack) > 0:
            self.generateNextStep()
        

    def generateNextStep(self):
        if self.started == True and len(self.nodeStack) == 0:
            return None, None

        self.started = True
        self.currentNode.visited = True
        neighbours = list(self.getNonVisitedNeighbourNodes(self.currentNode))
        if(len(neighbours) == 0):
            lastNode = self.currentNode
            self.currentNode = self.nodeStack.pop()
            return lastNode, True

        nextRandom = rnd.randint(0, len(neighbours)-1)
        nextNode = neighbours[nextRandom]
        self.currentNode.nodes.append(nextNode)
        nextNode.nodes.append(self.currentNode)
        self.nodeStack.append(self.currentNode)
        self.currentNode = nextNode
        return self.nodeStack[len(self.nodeStack)-1], False
    
    def getNonVisitedNeighbourNodes(self, node):
        if node.x > 0 and self.nodes[node.x-1][node.y].visited == False:
            yield self.nodes[node.x-1][node.y]
        if node.x+1 < self.width and self.nodes[node.x+1][node.y].visited == False:
            yield self.nodes[node.x+1][node.y]
        if node.y > 0 and self.nodes[node.x][node.y-1].visited == False:
            yield self.nodes[node.x][node.y-1]
        if node.y+1 < self.height and self.nodes[node.x][node.y+1].visited == False:
            yield self.nodes[node.x][node.y+1]

class Node():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.nodes = []
