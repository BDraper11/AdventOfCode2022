from AoC2022 import *
import re
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def StartingInput(): # Because I can't be arsed to code that interpreter.
    Stacks = [
        ['S','C','V','N'],
        ['Z','M','J','H','N','S'],
        ['M','C','T','G','J','N','D'],
        ['T','D','F','J','W','R','M'],
        ['P','F','H'],
        ['C','T','Z','H','J'],
        ['D','P','R','Q','F','S','L','Z'],
        ['C','S','L','H','D','F','P','W'],
        ['D','S','M','P','F','N','G','Z']
        ]
    return Stacks
def InputProcesing(input):
    ProcessedInput = input[10:]
    return ProcessedInput
def ParseDigits(input):
    InstructionSet = []
    for line in input:
        InstructionSet.append(re.findall(r'\d+',line))
    return InstructionSet
def Puzz1(Stacks, InstructionSet,Reverse=1):
    def ProcessMove(Stacks,NumCrates,StartStackId,EndStackId):
        Crates = Stacks[StartStackId][-NumCrates:]
        Stacks[StartStackId] = Stacks[StartStackId][:-NumCrates]
        if Reverse:
            Crates.reverse()
        Stacks[EndStackId].extend(Crates)
        return Stacks
    for Instruction in InstructionSet:
        NumCrates = int(Instruction[0])
        StartStackId = int(Instruction[1])-1
        EndStackId = int(Instruction[2])-1
        Stacks = ProcessMove(Stacks,NumCrates,StartStackId,EndStackId)
    TopCrateList = ''
    for Stack in Stacks:
        TopCrateList = TopCrateList+Stack[-1]
    return TopCrateList
def Puzz2(Stacks, InstructionSet,Reverse=1):
    Puzz2Ans = Puzz1(Stacks, InstructionSet,Reverse)
    return Puzz2Ans

if __name__ == "__main__":
    input = GetInput(1,5)
    Stacks = StartingInput()
    input = InputProcesing(input)
    InstructionSet = ParseDigits(input)
    Puzz1Ans = Puzz1(Stacks, InstructionSet)
    print("P1Ans: ",Puzz1Ans), pyperclip.copy(Puzz1Ans)
    Stacks = StartingInput() #Need to reinstantiate Stacks as it seems to get modified globally.
    Puzz2Ans = Puzz2(Stacks, InstructionSet,0)
    print("P2Ans: ",Puzz2Ans), pyperclip.copy(Puzz2Ans)