from collections import defaultdict

def default_value():
    return 0;

def process_input():
    with open('input') as file:
        inFile = file.read()
        return inFile

if __name__ == "__main__":
    input = process_input().strip()

    signal = []
    table = defaultdict(default_value)

    for i in range(len(input)):
        signal = input[i:i+14]
        distinct = set()
        print(signal)
        for j in signal:
            distinct.add(j)
        print(distinct)
        if(len(distinct) == 14):
            print(i)
            print(signal)
            break
