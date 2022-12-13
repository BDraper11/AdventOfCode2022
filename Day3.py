from AoC2022 import *
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
class Rucksack:
    def __init__(self,input):
        def DetCompartmentsContents(self):
            Compartment1 = self.Contents[:self.ContentsHalfwayIdx]
            Compartment2 = self.Contents[self.ContentsHalfwayIdx:]
            return Compartment1,Compartment2
        def DetIntersectionOfCompartments(self):
            return next(iter(set(self.Compartment1).intersection(set(self.Compartment2))))


        self.Contents = input
        self.ContentsLength = len(input)        
        self.ContentsHalfwayIdx = self.ContentsLength//2
        if (self.ContentsLength % 2) != 0:
            logging.info('\n\t\tNone even number of contents detected: %d\n\t\tHalfway Index set as: %d',self.ContentsLength,self.ContentsHalfwayIdx)
        self.Compartment1 = DetCompartmentsContents(self)[0]
        self.Compartment2 = DetCompartmentsContents(self)[1]
        self.CompartmentIntersection = DetIntersectionOfCompartments(self)
    def GetMispackedItem(self):
        return self.CompartmentIntersection
class ElfGroup:
    def __init__(self,input):
        def DetCommonItem(self):
            CommonItem = None
            for Rucksack in self.GroupRucksacks:
                if (not(type(CommonItem))==type(set())):
                    CommonItem = set(Rucksack.Contents)
                else:
                    CommonItem = CommonItem.intersection(set(Rucksack.Contents))
            return CommonItem
        self.GroupRucksacks = input
        self.CommonItem = DetCommonItem(self)
    def GetCommonItem(self):
        return self.CommonItem
def DetItemValue(input):
        if input.islower():
            return ord(input) - 96
        elif input.isupper():
            return ord(input) - 64 + 26
        else:
            logging.info('\n\t\tFailed to detect Uppercase or Lowercase input: %s',input)
def DetRucksackList(input):
    RucksackList = []
    for line in input:
        RucksackList.append(Rucksack(line))
    return RucksackList
def DetMispackedItemList(RucksackList):
    MispackedItemList = []
    for thisRucksack in RucksackList:
        MispackedItemList.append([thisRucksack.GetMispackedItem(),DetItemValue(thisRucksack.CompartmentIntersection)])
    return MispackedItemList
def Puzz1(RucksackList):
    MispackedItemList = DetMispackedItemList(RucksackList)
    return sum([x[1] for x in MispackedItemList])
def DetElfGroupList(RucksackList):
    ElfGroupList = []
    for RucksacksSets in range(len(RucksackList)//3):
        ElfGroupList.append(ElfGroup(RucksackList[:3]))
        RucksackList = RucksackList[3:]
    return ElfGroupList
def Puzz2(input):
    return sum([DetItemValue(next(iter(x.CommonItem))) for x in ElfGroupList])
if __name__ == "__main__":
    input = GetInput(1,3)

    RucksackList = DetRucksackList(input)    

    print("P1Ans: ",Puzz1(RucksackList)), pyperclip.copy(Puzz1(RucksackList))

    ElfGroupList = DetElfGroupList(RucksackList)

    print("P2Ans: ",Puzz2(input)), pyperclip.copy(Puzz2(input))