def process_input():
    with open('input') as file:
        inFile = file.read()
        return inFile


class Forest:
    def __init__(self, input):
        self.forest = []
        for line in input.split('\n'):
            row = []
            for height in line:
                row.append(int(height))
            self.forest.append(row)
        self.height = len(self.forest)
        self.width = len(self.forest[0])


    def check_edge(self, i, j):
        if (i == 0) or (j == 0) or (i == self.height - 1) or (j == self.width - 1):
            return True

    def check_top(self, x, y):
        visibility = True
        for i in range(x - 1, -1, -1):
            if self.forest[i][y] >= self.forest[x][y]:
                visibility = False
        return visibility


    def check_left(self, x, y):
        visibility = True
        for i in range(y - 1, -1, -1):
            if self.forest[x][i] >= self.forest[x][y]:
                visibility = False
        return visibility


    def check_bottom(self, x, y):
        visibility = True
        for i in range(x + 1, self.height, 1):
            if self.forest[i][y] >= self.forest[x][y]:
                visibility = False
        return visibility


    def check_right(self, x, y):
        visibility = True
        for i in range(y + 1, self.width, 1):
            if self.forest[x][i] >= self.forest[x][y]:
                visibility = False
        return visibility


    def check_visibility(self, x, y):
        if self.check_edge(x, y):
            return True
        elif self.check_top(x, y):
            return True
        elif self.check_left(x, y):
            return True
        elif self.check_bottom(x, y):
            return True
        elif self.check_right(x, y):
            return True
        else:
            return False


    def find_visible_trees(self):
        visible_trees = 0
        for i in range(self.height):
            for j in range(self.width):
                if (self.check_visibility(i, j)):
                    visible_trees += 1
        return visible_trees

    def print(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.forest[i][j], end="")
            print()

if __name__ == "__main__":
    input = process_input().strip()
    forest = Forest(input)
    forest.print()
    print(forest.find_visible_trees())

