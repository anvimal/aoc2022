import queue

def get_stack_info(input):
    lineno = 0
    for i in input:
        print(i)
        if i == '':
            break;
        lineno += 1
    num_stacks =  int(input[lineno-1].strip().split(' ')[-1])
    stacks = []
    for i in range(lineno):
        stacks.append([])
    print(stacks)

    for i in range(lineno-1):
        for j in range(num_stacks):
            container = input[i][4*j+1]
            if (container != ' '):
                stacks[j].append(container)

    for i in range(num_stacks):
        stacks[i].reverse()
    print(stacks)
    return lineno, stacks

def perform_operation(input, lineno, stacks):
    print(input[lineno])
    command = input[lineno].strip().split(' ')
    num_containers = int(command[1])
    source = int(command[3])
    target = int(command[5])

    print(num_containers, source, target)

    for i in range(num_containers):
        temp = stacks[source-1].pop()
        stacks[target-1].append(temp)
    print(stacks)

def perform_operation_new(input, lineno, stacks):
    print(input[lineno])
    command = input[lineno].strip().split(' ')
    num_containers = int(command[1])
    source = int(command[3])
    target = int(command[5])

    print(num_containers, source, target)
    temp = []
    for i in range(num_containers):
        temp.append(stacks[source-1].pop())
    for i  in range(num_containers):
        stacks[target-1].append(temp.pop())
    print(stacks)


def process_input():
    with open('input') as file:
        inFile = file.read()
        return inFile
if __name__ == "__main__":
    inFile = process_input()
    input = inFile.strip().split('\n')
    lineno, stacks = get_stack_info(input)
    for i in range(lineno+1, len(input)):
        perform_operation_new(input, i, stacks)
    for i in range(len(stacks)):
        print(stacks[i][-1])