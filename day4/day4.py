
def totally_subsumed(entry):
    ranges = entry.split(',')
    elf1_range = ranges[0].split('-')
    elf2_range = ranges[1].split('-')

    elf1 = list(map(lambda x:int(x), elf1_range))
    elf2 = list(map(lambda x:int(x), elf2_range))

    elf1_set = set()
    elf2_set = set()
    for i in range(elf1[0], elf1[1]+1):
        elf1_set.add(i)
    for i in range(elf2[0], elf2[1]+1):
        elf2_set.add(i)
    print(elf1, elf2)
    print (elf1_set, elf2_set)
    print(elf1_set.intersection(elf2_set))
    print(len(elf1_set.intersection(elf2_set)))
    if (len(elf1_set.intersection(elf2_set)) > 0):
        return 1
    print("returning 0")
    return 0
    '''
    if (((elf1[0] >= elf2[0]) and (elf1[1] <= elf2[1])) or
        ((elf2[0] >= elf1[0]) and (elf2[1] <= elf1[1]))):
        return 1
    return 0
    '''

def process_input():
    with open('input') as file:
        inFile = file.read()
        return inFile

if __name__ == "__main__":
    inFile = process_input()
    tally = 0
    for entry in inFile.strip().split('\n'):
        tally += totally_subsumed(entry)
    print(tally)
    print(len(inFile.strip().split('\n')))