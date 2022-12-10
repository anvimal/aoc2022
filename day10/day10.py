

def process_input():
    with open('input') as file:
        inFile = file.read()
        return inFile.strip()

if __name__ == "__main__":
    input = process_input()

    cycle = []
    X = 1
    for i in input.split('\n'):
        cmd = i.split(' ')
        if cmd[0] == "noop":
            cycle.append(X)
        elif cmd[0] == "addx":
            value = int(cmd[1])
            cycle.append((X))
            cycle.append((X))
            X += value
    print(len(cycle))
    print(cycle)
    total = 0
    for i in range(20,260, 40):
        total += cycle[i-1]*i
    print(total)

    for i in range(6):
        for j in range(40):
            index = i*40 + j
            sprite = cycle[index]
            if (j >= (sprite-1)) and (j <= (sprite+1)):
                print('#', end="")
            else:
                print(".", end="")
        print()
    print()



