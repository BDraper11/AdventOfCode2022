from AoC2022 import *
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

class ElfPair:
    def __init__(self,input):
        def ParseInput(input):
            input = input.split(',')
            return input

        def DetElves(input):
            Elves = []
            for element in input:
                Elves.append(self.Elf(element))
            return Elves

        def DetFullContained(input):
            logic1 = input[0].SectionAssignment.issubset(input[1].SectionAssignment)
            logic2 = input[1].SectionAssignment.issubset(input[0].SectionAssignment)
            return (logic1 or logic2)

        def DetAnyOverlap(input):
            return not(input[0].SectionAssignment.isdisjoint(input[1].SectionAssignment))

        self.input = ParseInput(input)
        self.Elves = DetElves(self.input)
        self.FullContained = DetFullContained(self.Elves)
        self.AnyOverlap = DetAnyOverlap(self.Elves)
        return

    class Elf:
        def __init__(self,input):
            self.RangeHi = int(input.split('-')[1])
            self.RangeLo = int(input.split('-')[0])
            self.SectionAssignment = set(range(self.RangeLo,self.RangeHi+1))
            return

def DetElfPairList(input):
    ElfPairList = []
    for line in input:
        ElfPairList.append(ElfPair(line))
    return ElfPairList



def Puzz1(input):
    sumAns = 0
    for x in ElfPairList: # (sum[int(x.FullContained)] for x in ElfPairList)
        sumAns += int(x.FullContained)
    return sumAns

def Puzz2(input):
    sumAns = 0
    for x in ElfPairList: # (sum[int(x.FullContained)] for x in ElfPairList)
        sumAns += int(x.AnyOverlap)
    return sumAns

if __name__ == "__main__":
    input = GetInput(1,4)
    ElfPairList = DetElfPairList(input)
    Puzz1Ans = Puzz1(ElfPairList)
    print("P1Ans: ",Puzz1Ans), pyperclip.copy(Puzz1Ans)
    Puzz2Ans = Puzz2(ElfPairList)
    print("P2Ans: ",Puzz2Ans), pyperclip.copy(Puzz2Ans)