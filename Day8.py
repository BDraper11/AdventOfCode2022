from AoC2022 import *
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def InputProcessing(input):
    output = []
    for row in input:
        output.append(list(row))
    return output

def GetNumPerimeterTrees(input):
    xLen = len(input[0])
    yLen = len(input)
    NumPerimeterTrees = 2*xLen+2*(yLen-2)
    return NumPerimeterTrees

def GetCandidateTrees(input):
    CandidateTrees = input[1:-1]
    for row in CandidateTrees:
        del row[0]
        del row [-1]
    return CandidateTrees

def GetPerimeters(input): # Effectievly, ditch the corners.
    def GetNorthPerimeter(input):
        Perimeter = input[0]
        del Perimeter[0]
        del Perimeter[-1]
        return Perimeter
    def GetSouthPerimeter(input):
        Perimeter = input[-1]
        del Perimeter[0]
        del Perimeter[-1]
        return Perimeter
    def GetEastPerimeter(input):
        input = input[1:-1]
        Perimeter = []
        for row in input:
            Perimeter.append(row[-1])
        return Perimeter
    def GetWestPerimeter(input):
        input = input[1:-1]
        Perimeter = []
        for row in input:
            Perimeter.append(row[0])
        return Perimeter
    NorthPerimeter = GetNorthPerimeter(input)
    SouthPerimeter = GetSouthPerimeter(input)
    EastPerimeter = GetEastPerimeter(input)
    WestPerimeter = GetWestPerimeter(input)
    return NorthPerimeter,SouthPerimeter, EastPerimeter, WestPerimeter

def DetVisible(CandidateTrees,Perimeters):
    def EasterlySearch(Perimeter,pIdx,CandidateTrees,gIdx,element):
        if gIdx>0:
            interstitialTreesTallest = max(CandidateTrees[pIdx][:gIdx])
            if element>Perimeter[pIdx] and element>interstitialTreesTallest:
                Visible = True
            else:
                Visible = False
        else:
            if element>Perimeter[pIdx]:
                Visible = True
            else:
                Visible = False
        return Visible
    def WesterlySearch(Perimeter,pIdx,CandidateTrees,gIdx,element):
        if gIdx<len(CandidateTrees[pIdx])-1:
            interstitialTreesTallest = max(CandidateTrees[pIdx][gIdx+1:])
            if element>Perimeter[pIdx] and element>interstitialTreesTallest:
                Visible = True
            else:
                Visible = False
        else:
            if element>Perimeter[pIdx]:
                Visible = True
            else:
                Visible = False
        return Visible
    def SoutherlySearch(Perimeter,pIdx,CandidateTrees,gIdx,element):
        if gIdx>0:
            interstitialTreesTallest = max([row[pIdx] for row in CandidateTrees][:gIdx])
            if element>Perimeter[pIdx] and element>interstitialTreesTallest:
                Visible = True
            else:
                Visible = False
        else:
            if element>Perimeter[pIdx]:
                Visible = True
            else:
                Visible = False
        return Visible
    def NortherlySearch(Perimeter,pIdx,CandidateTrees,gIdx,element):
        if gIdx<len(CandidateTrees)-1:
            interstitialTreesTallest = max([row[pIdx] for row in CandidateTrees][gIdx+1:])
            if element>Perimeter[pIdx] and element>interstitialTreesTallest:
                Visible = True
            else:
                Visible = False
        else:
            if element>Perimeter[pIdx]:
                Visible = True
            else:
                Visible = False
        return Visible
    countVisibleCandidates = 0
    for rIdx,row in enumerate(CandidateTrees):
        for eIdx,element in enumerate(row):
            print(eIdx,rIdx,element)
            eVisible = EasterlySearch(Perimeters[3],rIdx,CandidateTrees,eIdx,element)
            wVisible = WesterlySearch(Perimeters[2],rIdx,CandidateTrees,eIdx,element)
            sVisible = SoutherlySearch(Perimeters[0],eIdx,CandidateTrees,rIdx,element)
            nVisible = NortherlySearch(Perimeters[1],eIdx,CandidateTrees,rIdx,element)
            isVisible = any([eVisible,wVisible,sVisible,nVisible])
            if isVisible:
                countVisibleCandidates +=1
    return countVisibleCandidates

def DetScenicScore(CandidateTrees,Perimeters):
    def WesterlyViewRange(Perimeter,pIdx,CandidateTrees,gIdx,element):
        interstitialTrees = [Perimeter[pIdx]]
        if CandidateTrees[pIdx][:gIdx] != []:
            interstitialTrees = interstitialTrees+CandidateTrees[pIdx][:gIdx]
        interstitialTrees.reverse()
        ViewRange = 0
        for tree in interstitialTrees:
            if tree<element:
                ViewRange +=1
            else:
                ViewRange +=1
                break
        return ViewRange
    def EasterlyViewRange(Perimeter,pIdx,CandidateTrees,gIdx,element):
        if CandidateTrees[pIdx][gIdx+1:] != []:
            interstitialTrees = CandidateTrees[pIdx][gIdx+1:]+[Perimeter[pIdx]]
        else:
            interstitialTrees = [Perimeter[pIdx]]
        ViewRange = 0
        for tree in interstitialTrees:
            if tree<element:
                ViewRange +=1
            else:
                ViewRange +=1
                break
        return ViewRange
    def SoutherlyViewRange(Perimeter,pIdx,CandidateTrees,gIdx,element):
        if CandidateTrees[pIdx][gIdx+1:] != []:
            interstitialTrees = [row[pIdx] for row in CandidateTrees][gIdx+1:]+[Perimeter[pIdx]]
        else:
            interstitialTrees = [Perimeter[pIdx]]
        ViewRange = 0
        for tree in interstitialTrees:
            if tree<element:
                ViewRange +=1
            else:
                ViewRange +=1
                break
        return ViewRange
    def NortherlyViewRange(Perimeter,pIdx,CandidateTrees,gIdx,element):
        if CandidateTrees[pIdx][:gIdx] != []:
            interstitialTrees = [Perimeter[pIdx]]+[row[pIdx] for row in CandidateTrees][:gIdx]
        else:
            interstitialTrees = [Perimeter[pIdx]]
        interstitialTrees.reverse()
        ViewRange = 0
        for tree in interstitialTrees:
            if tree<element:
                ViewRange +=1
            else:
                ViewRange +=1
                break
        return ViewRange
    ScenicScore = 0
    for rIdx,row in enumerate(CandidateTrees):
        for eIdx,element in enumerate(row):
            #print(eIdx,rIdx,element)
            wViewRange = WesterlyViewRange(Perimeters[3],rIdx,CandidateTrees,eIdx,element)
            eViewRange = EasterlyViewRange(Perimeters[2],rIdx,CandidateTrees,eIdx,element)
            sViewRange = SoutherlyViewRange(Perimeters[1],eIdx,CandidateTrees,rIdx,element)
            nViewRange = NortherlyViewRange(Perimeters[0],eIdx,CandidateTrees,rIdx,element)
            #print(nViewRange,eViewRange,sViewRange,wViewRange)
            if (ScenicScore<(eViewRange*wViewRange*sViewRange*nViewRange)):
                ScenicScore = eViewRange*wViewRange*sViewRange*nViewRange
    return ScenicScore


def Puzz1(input):
    logging.info('Grid Size: %dx by %dy',len(input[0]),len(input))
    NumPerimeterTrees = GetNumPerimeterTrees(input)
    logging.info('NumPerimeterTrees = %d',NumPerimeterTrees)
    Perimeters = GetPerimeters(input)
    CandidateTrees = GetCandidateTrees(input)
    countVisibleCandidates = DetVisible(CandidateTrees,Perimeters)
    return NumPerimeterTrees+countVisibleCandidates
def Puzz2(input):
    Perimeters = GetPerimeters(input)
    CandidateTrees = GetCandidateTrees(input)
    return DetScenicScore(CandidateTrees,Perimeters)

if __name__ == "__main__":
    input = GetInput(8)
    input = InputProcessing(input)
    Puzz1Ans = Puzz1(input)
    print("P1Ans: ",Puzz1Ans), pyperclip.copy(Puzz1Ans)
    Puzz2Ans = Puzz2(input)
    print("P2Ans: ",Puzz2Ans), pyperclip.copy(Puzz2Ans)