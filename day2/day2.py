from functools import *
from enum import Enum

class Choice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Score(Enum):
    LOST = 0
    DRAW = 3
    WIN = 6

class OppChoice:
    def __init__(self, choice):
        if (choice == 'A'):
            self._choice = Choice.ROCK
        elif (choice == 'B'):
            self._choice = Choice.PAPER
        else:
            self._choice = Choice.SCISSORS

    def value(self):
        return self.choice.value
    def choice(self):
        return self._choice
'''
class MyChoice:
    def __init__(self, choice):
        if (choice == 'X'):
            self._choice = Choice.ROCK
        elif (choice == 'Y'):
            self._choice = Choice.PAPER
        else:
            self._choice = Choice.SCISSORS

    def value(self):
        return self._choice.value
    def choice(self):
        return self._choice
'''

class MyChoice:
    def __init__(self, opp_choice, result):
        if (result == 'Y'):
            self._choice = opp_choice.choice()
        elif (result == 'X'):
            if opp_choice.choice() == Choice.ROCK:
                self._choice = Choice.SCISSORS
            elif opp_choice.choice() == Choice.SCISSORS:
                self._choice = Choice.PAPER
            else:
                self._choice = Choice.ROCK
        else:
            if opp_choice.choice() == Choice.ROCK:
                self._choice = Choice.PAPER
            elif opp_choice.choice() == Choice.SCISSORS:
                self._choice = Choice.ROCK
            else:
                self._choice = Choice.SCISSORS

    def value(self):
        return self._choice.value
    def choice(self):
        return self._choice


def result_of_round(opp_choice, my_choice):
    if opp_choice.choice() == my_choice.choice():
        return 3
    elif ((opp_choice.choice() == Choice.ROCK and my_choice.choice() == Choice.PAPER) or
        (opp_choice.choice() == Choice.PAPER and my_choice.choice() == Choice.SCISSORS) or
        (opp_choice.choice() == Choice.SCISSORS and my_choice.choice() == Choice.ROCK)):
        return 6
    else:
        return 0

def tally_round(entry):
    choice = entry.split(' ')
    print(choice)
    opp_choice = OppChoice(choice[0])
    my_choice = MyChoice(opp_choice, choice[1])
    result = result_of_round(opp_choice, my_choice)
    print(result, my_choice.value())
    return result + my_choice.value()

def process_input():
    with open('input') as file:
        inFile = file.read()
        return inFile

if __name__ == "__main__":
    inFile = process_input()
    my_score = 0
    for entry in inFile.strip().split('\n'):
        my_score += tally_round(entry)
    print(my_score)