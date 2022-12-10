from functools import *

def common_rucksack_item(rucksack):
    comp1 = set(rucksack[:int(len(rucksack)/2)])
    comp2 = set(rucksack[int(len(rucksack)/2):])
    for i in comp1.intersection(comp2):
        return i

def group_badge(bag1, bag2, bag3):
    for i in set(bag1).intersection(set(bag2)).intersection(set(bag3)):
        return i

def item_to_priority(item):
    priority = 0
    if (item.islower()):
        priority = ord(item) - ord('a') + 1
    else:
        priority = ord(item) - ord('A') + 27
    print(item, priority)
    return priority

def process_input():
    with open('input') as file:
        inFile = file.read()
        return inFile

if __name__ == "__main__":
    inFile = process_input()
    total = 0
    bags = inFile.strip().split('\n')
    for group in range(int(len(bags)/3)):
        bag1 = bags[3 * group]
        bag2 = bags[3 * group + 1]
        bag3 = bags[3 * group + 2]
        badge = group_badge(bag1, bag2, bag3)
        total += item_to_priority(badge)
    print(total)