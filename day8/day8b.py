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

    def top_value(self, x, y):
        value = 1
        for i in range(x - 1, 0, -1):
            if self.forest[i][y] < self.forest[x][y]:
                value += 1
            else:
                break
        return value

    def left_value(self, x, y):
        value = 1
        for i in range(y - 1, 0, -1):
            if self.forest[x][i] < self.forest[x][y]:
                value += 1
            else:
                break
        return value

    def bottom_value(self, x, y):
        value = 1
        for i in range(x + 1, self.height-1, 1):
            if self.forest[i][y] < self.forest[x][y]:
                value += 1
            else:
                break
        return value

    def right_value(self, x, y):
        value = 1
        for i in range(y + 1, self.width-1, 1):
            if self.forest[x][i] < self.forest[x][y]:
                value += 1
            else:
                break
        return value

    def sceinic_value(self, x, y):
        if self.check_edge(x, y):
            return 0
        else:
            top_value = self.top_value(x, y)
            left_value = self.left_value(x, y)
            bottom_value = self.bottom_value(x, y)
            right_value = self.right_value(x, y)
            total_value = top_value * left_value * bottom_value * right_value

            #print("coord [{0},{1}] -> [{2},{3},{4},{5}] -> {6}".format(x,y,top_value,left_value,bottom_value,right_value, total_value))
            return total_value

    def find_most_scenic_value(self):
        max_value = 0
        for i in range(self.height):
            for j in range(self.width):
                value = self.sceinic_value(i, j)
                if value > max_value:
                    max_value = value
                    print("New Max Value = {0} at [{1},{2}]".format(max_value, i, j))
        return value

    def print(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.forest[i][j], end="")
            print()

if __name__ == "__main__":
    input = process_input().strip()
    forest = Forest(input)
    forest.print()
    print(forest.find_most_scenic_value())
