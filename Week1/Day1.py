from AoC2022 import *
import logging, sys

def Day1Puz1():
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
def Day1Puz2(ElfList):
    ElfList.sort(reverse=True)
    ThreeElfCalories = sum(ElfList[0:3])
    return ThreeElfCalories



if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    logging.debug('A debug message!')
    logging.info('We processed %d records', len([1,2,3,4]))
    
    input = GetInput()
    print("D1P1Ans: ",Day1Puz1()[0])
    print("D1P2Ans: ",Day1Puz2(Day1Puz1()[1]))
    print("Done")