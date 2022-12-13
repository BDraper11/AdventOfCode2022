from AoC2022 import *

def Puzz1(input):
    CalorieCount = 0
    ElfList = []
    MaxCalories = 0
    for line in input:
        if not(line.isnumeric()):
            ElfList.append(CalorieCount)
            CalorieCount = 0
        else:
            CalorieCount += int(line)
    for Elf in ElfList:
        MaxCalories = max(MaxCalories,Elf)
    return MaxCalories, ElfList
def Puzz2(ElfList):
    ElfList.sort(reverse=True)
    ThreeElfCalories = sum(ElfList[0:3])
    return ThreeElfCalories

if __name__ == "__main__":
    input = GetInput(1,1)
    print("D1P1Ans: ",Puzz1(input)[0])
    print("D1P2Ans: ",Puzz2(Puzz1()[1]))