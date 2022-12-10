from enum import Enum

def process_input():
    with open('input') as file:
        inFile = file.read()
        return inFile

class Knot:
    def __init__(self, index, prior=None, follower=None):
        self.visited = set()
        self.prior = prior
        self.follower = follower
        self.index = index
        self.X = self.Y = 0

        coord = (self.X, self.Y)
        self.visited.add(coord)

    def moveKnot(self):
        #print("Knot{0} at ({1}, {2})".format(self.prior.index, self.prior.X, self.prior.Y))
        #print("Knot{0} at ({1}, {2})".format(self.index, self.X, self.Y))
        lX = self.prior.X
        lY = self.prior.Y
        kX = self.X
        kY = self.Y
        assert(max(lX, kX) - min(lX, kX) <= 2)
        assert(max(lY, kY) - min(lY, kY) <= 2)
        if (max(lX, kX) - min(lX, kX) <= 1) and (max(lY, kY) - min(lY, kY) <=1):
            return
        elif self.prior.X == self.X:
            if self.prior.Y > self.Y:
                self.Y += 1
            else:
                self.Y -= 1
        elif self.prior.Y == self.Y:
            if self.prior.X > self.X:
                self.X += 1
            else:
                self.X -= 1
        else:
            if self.prior.X > self.X:
                self.X += 1
            else:
                self.X -= 1
            if self.prior.Y > self.Y:
                self.Y += 1
            else:
                self.Y -= 1

        coord = (self.X, self.Y)
        #print("Knot{0} moved to {1}".format(self.index, coord))
        self.visited.add(coord)
        if self.follower is not None:
            self.follower.moveKnot()

    def moveLeft(self, offset):
        for i in range(1, offset+1):
            self.X += 1
            self.follower.moveKnot()

    def moveRight(self, offset):
        for i in range(1, offset+1):
            self.X -= 1
            self.follower.moveKnot()

    def moveUp(self, offset):
        for i in range(1, offset+1):
            self.Y += 1
            self.follower.moveKnot()

    def moveDown(self, offset):
        for i in range(1, offset+1):
            self.Y -= 1
            self.follower.moveKnot()

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
        #print(self.visited)
        return len(self.visited)

if __name__ == "__main__":
    input = process_input().strip()
    prior = None
    knots = []
    for i in range(2):
        knot = Knot(i, prior=prior)
        if prior is not None:
            prior.follower = knot
        prior = knot
        knots.append(knot)
    knots[0].executeMoves(input)
    print(knots[-1].uniqueTailCoords())
    #print(knots)