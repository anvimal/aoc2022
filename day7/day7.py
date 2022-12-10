from enum import Enum
from functools import *

class ContentType(Enum):
    FILE = 1
    DIR = 2

class File:
    def __init__(self, name, size):
        self.name = name
        self.type = ContentType.FILE
        self.size = int(size)

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.type = ContentType.DIR
        self.children = []
        self.parentDir = parent

    def add_child(self, child):
        self.children.append(child)

    def find_size(self):
        size = 0
        for i in self.children:
            if i.type == ContentType.FILE:
                size += i.size
            else:
                size += i.find_size()
        self.size = size
        return size

    def parent(self):
        return self.parentDir

    def traverse(self, space):
        for i in self.children:
            if i.type == ContentType.FILE:
                print("{0}{1} {2}".format(space, i.name, i.size))
            else:
                print("{0}{1}/".format(space, i.name))
                i.traverse(space+" "*4)

root = Directory('/', None)

problem_1_sum = 0

def traverse_with_size(directory):
    global problem_1_sum
    for i in directory.children:
        if i.type == ContentType.DIR:
            if i.size <= 100000:
                problem_1_sum += i.size
            traverse_with_size(i)

current_smallest = 70000000
def find_most_optimal(directory, need_to_free):
    global current_smallest
    for i in directory.children:
        if i.type == ContentType.DIR:
            if i.size >= need_to_free and i.size < current_smallest:
                current_smallest = i.size
            find_most_optimal(i, need_to_free)


def parse_input(input):
    currentDir = root
    parentDir  = None
    for cmd in input:
        cmd = cmd.strip()
        print("Current Directory is {0}".format(currentDir.name))
        if (len(cmd) > 2 and cmd[:2] == "cd"):
            print("CD command")
            dir_name = cmd.strip().split(' ')[1]
            if dir_name == "/":
                print("Change directory to /")
                currentDir = root
                parentDir = None
            elif dir_name == "..":
                currentDir = parentDir
                parentDir = currentDir.parent()
                if parentDir == None and currentDir.name == "/":
                    print("Current Directory is {0}".format(currentDir.name))
                else:
                    print("Change to parent directory. Current directory = {0}, Parent Directory = {1}".format(currentDir.name, parentDir.name))
            else:
                found = False
                for entry in currentDir.children:
                    if (entry.name == dir_name) and (entry.type == ContentType.DIR):
                        parentDir = currentDir
                        currentDir = entry
                        found = True
                        print("Change to directory {0}".format(dir_name))
                        break
                if not found:
                    print(cmd)
                    assert(0)
        elif len(cmd) > 2 and cmd[:2] == "ls":
            print("LS command")
            contents = cmd.strip().split('\n')
            for entry in contents[1:]:
                if entry[:3] == "dir":
                    dirEntry = entry.strip().split(' ')
                    name = dirEntry[1]
                    found = False
                    for existingEntry in currentDir.children:
                        if existingEntry.name == name:
                            found = True
                    if not found:
                        newDir = Directory(name, currentDir)
                        currentDir.children.append(newDir)
                        print("Found new Directory {}".format(name))
                else:
                    fileEntry = entry.strip().split(' ')
                    size = fileEntry[0]
                    name = fileEntry[1]
                    found = False
                    for existingEntry in currentDir.children:
                        if existingEntry.name == name:
                            found = True
                    if not found:
                        newFile = File(name, size)
                        currentDir.children.append(newFile)
                        print("Found new File {}".format(name))
def process_input():
    with open('input') as file:
        inFile = file.read()
        return inFile

if __name__ == "__main__":
    input = process_input().strip().split('$')
    input = list(map(lambda x: x.strip(), input))
    parse_input(input)
    print(root.name)
    root.traverse(" "*4)
    root.find_size()
    usage = root.size
    free_space = 70000000-usage
    print(free_space)
    need_to_free = 30000000 - free_space
    print(need_to_free)
    find_most_optimal(root, need_to_free)
    print(current_smallest)
