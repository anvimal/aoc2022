from enum import Enum

def process_input():
    with open('input') as file:
        inFile = file.read()
        return inFile

class Direction(Enum):
    DOWN = 0,
    LEFT = 1,
    UP = 2,
    RIGHT = 3

class Grid:
    def __init__(self):
        self.visited = set()
        self.headX = self.headY = 0
        self.tailX = self.tailY = 0

        coord = (self.tailX, self.tailY)
        self.visited.add(coord)
        print(self.visited)

    def grid_size(self):
        ver = hor = 0
        maxVer = minVer = maxHor = minHor = 0
        for cmd in input.split("\n"):
            move = cmd.strip().split(" ")
            if move[0] == "L":
                hor += int(move[1])
                maxHor = max(hor, maxHor)
            elif move[0] == "R":
                hor -= int(move[1])
                minHor = min(hor, minHor)
            elif move[0] == "U":
                ver += int(move[1])
                maxVer = max(ver, maxVer)
            elif move[0] == "D":
                ver -= int(move[1])
                minVer = min(ver, minVer)
        print(ver, hor, maxHor, minHor, maxVer, minVer)

    def moveTail(self):
        print("Head at ({0}, {1})".format(self.headX, self.headY))
        print("Tail at ({0}, {1})".format(self.tailX, self.tailY))
        hX = self.headX
        hY = self.headY
        tX = self.tailX
        tY = self.tailY
        assert(max(hX, tX) - min(hX,tX) <= 2)
        assert(max(hY, tY) - min(hY,tY) <= 2)
        if (max(hX, tX) - min(hX, tX) <= 1) and (max(hY, tY) - min(hY, tY) <=1):
            return
        elif self.headX == self.tailX:
            if self.headY > self.tailY:
                self.tailY += 1
            else:
                self.tailY -= 1
        elif self.headY == self.tailY:
            if self.headX > self.tailX:
                self.tailX += 1
            else:
                self.tailX -= 1
        else:
            if self.headX > self.tailX:
                self.tailX += 1
            else:
                self.tailX -= 1
            if self.headY > self.tailY:
                self.tailY += 1
            else:
                self.tailY -= 1

        coord = (self.tailX, self.tailY)
        print("Tail moved to {}".format(coord))
        self.visited.add(coord)

    def moveLeft(self, offset):
        for i in range(1, offset+1):
            self.headX += 1
            self.moveTail()

    def moveRight(self, offset):
        for i in range(1, offset+1):
            self.headX -= 1
            self.moveTail()

    def moveUp(self, offset):
        for i in range(1, offset+1):
            self.headY += 1
            self.moveTail()

    def moveDown(self, offset):
        for i in range(1, offset+1):
            self.headY -= 1
            self.moveTail()

    def executeMoves(self, input):
        for cmd in input.split("\n"):
            move = cmd.strip().split(" ")
            if move[0] == "L":
                self.moveLeft(int(move[1]))
            elif move[0] == "R":
                self.moveRight(int(move[1]))
            elif move[0] == "U":
                self.moveUp(int(move[1]))
            elif move[0] == "D":
                self.moveDown(int(move[1]))

    def uniqueTailCoords(self):
        print(self.visited)
        return len(self.visited)

if __name__ == "__main__":
    input = process_input().strip()
    grid = Grid()
    grid.executeMoves(input)
    print(grid.uniqueTailCoords())
