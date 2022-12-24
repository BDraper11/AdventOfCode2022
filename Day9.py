import sys
if sys.version_info[0] < 3 or sys.version_info[0]==3 and sys.version_info[1]<10:
    raise Exception("Must be using Python 3.10 or greater")
from math import copysign
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator

from AoC2022 import *
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

class Knot:
    def __init__(self,KnotID,IsLast=False,origin=[0,0]):
        #self.Origin = origin
        self.Coords = list(origin)
        self.NextKnot = None
        self.History = list()
        self.UniqueHist = list()
        self.KnotID = int(KnotID)
        if IsLast:
            self.Type = "Last"
        else:
            self.Type = "Knot"
        self.UpdateKnotHistory(self.Coords)
    def AddNextKnot(self,IsLast=False):
        self.NextKnot = Knot(self.KnotID+1,IsLast)
    def SetCoord(self,newCoords):
        newCoords = list(newCoords)

        if newCoords != self.Coords:
            self.Coords = newCoords
            self.UpdateKnotHistory(newCoords)
    def UpdateKnotHistory(self,newCoords):
        newCoords = list(newCoords)
        global KnotPosArray
        KnotPosArray[self.KnotID] = newCoords
        self.History.append(newCoords)
        if newCoords not in self.UniqueHist:
            self.UniqueHist.append(newCoords)

    def UpdateFirstKnotPosition(self,FirstKnotCoords,Dir,Mag):
        FirstKnotCoords = list(FirstKnotCoords)
        for step in range(int(Mag)): # Go step by step through instruction updates.
            match Dir: # Make appropriate first knot move (position update).
                case 'U':
                    FirstKnotCoords[1] = FirstKnotCoords[1]+1
                case 'D':
                    FirstKnotCoords[1] = FirstKnotCoords[1]-1
                case 'L':
                    FirstKnotCoords[0] = FirstKnotCoords[0]-1
                case 'R':
                    FirstKnotCoords[0] = FirstKnotCoords[0]+1
            self.SetCoord(FirstKnotCoords) # Set the coordinate of the knot using the class method.
            self.NextKnot.UpdateTrailKnotPosition(self.Coords,self.NextKnot.Coords)
        return
    def UpdateTrailKnotPosition(self,LeadingKnotPosition,CurrKnotPos):
        CurrKnotPos = list(CurrKnotPos)
        offset = [a_i - b_i for a_i, b_i in zip(LeadingKnotPosition, CurrKnotPos)]
        if any(abs(x)>1 for x in offset):
            #print(offset)
            if CurrKnotPos[0]==LeadingKnotPosition[0]: # Are we in the same row?
                CurrKnotPos[1] = CurrKnotPos[1]+int(copysign(1,offset[1]))
            elif CurrKnotPos[1]==LeadingKnotPosition[1]: # Are we in the same column?
                CurrKnotPos[0] = CurrKnotPos[0]+int(copysign(1,offset[0]))
            elif abs(offset[0])>abs(offset[1]):
                CurrKnotPos[1] = LeadingKnotPosition[1] # Step into the same column.
                CurrKnotPos[0] = CurrKnotPos[0]+int(copysign(1,offset[0]))
            elif abs(offset[1])>abs(offset[0]):
                CurrKnotPos[0] = LeadingKnotPosition[0] # Step into the same row.
                CurrKnotPos[1] = CurrKnotPos[1]+int(copysign(1,offset[1]))
            elif abs(offset[0])==abs(offset[1]):
                CurrKnotPos[0] = CurrKnotPos[0]+int(copysign(1,offset[0]))
                CurrKnotPos[1] = CurrKnotPos[1]+int(copysign(1,offset[1]))
            else:
                print("Error")
        self.SetCoord(CurrKnotPos)
        if type(self.NextKnot) == type(Knot(0)):
            self.NextKnot.UpdateTrailKnotPosition(self.Coords,self.NextKnot.Coords)
        if self.KnotID == 9 and CurrKnotPos == [18, -7]:
            print ('Now')
        return CurrKnotPos

def InputProcessing(input):
    output = []
    for row in input:
        output.append([row.split()[0],int(row.split()[1])])
    return output
def Puzz1(input):
    return

def Puzz2(input):
    global KnotList, KnotPosArray
    KnotID = 0
    numKnots = 10
    KnotPosArray = [[i*0,i*0] for i in range(0,numKnots,1)]
    for k in range(numKnots): ## Build Knots.
        if len(KnotList)==0: # First Knot
            thisKnot = Knot(KnotID)
            FirstKnot = thisKnot
        elif len(KnotList)<(numKnots-1): # Interstitial Knots
            thisKnot.AddNextKnot()
            thisKnot = thisKnot.NextKnot
        elif len(KnotList)==(numKnots-1): # Last Knot
            thisKnot.AddNextKnot(True)
            thisKnot = thisKnot.NextKnot
        else:
            logging.info('\n\t\tError:\tIssue with number of knots being created')
        KnotList.append(thisKnot)
    for instruction in input: ## Action Instructions.
        match instruction[0]: ## Doesn't do anything important, just the logging print out.
            case 'U':
                logging.info('\t\tMove Up %s places',instruction[1])
            case 'D':
                logging.info('\t\tMove Down %s places',instruction[1])
            case 'L':
                logging.info('\t\tMove Left %s places',instruction[1])
            case 'R':
                logging.info('\t\tMove Right %s places',instruction[1])
        FirstKnot.UpdateFirstKnotPosition(FirstKnot.Coords,instruction[0],instruction[1])
        ## Trying to debug
        '''KnotPosArray = []
        for k in KnotList:
            KnotPosArray.append(k.Coords)'''
        if (0): # Plotting.
            data = np.array(KnotPosArray)
            x, y = data.T
            fig, ax = plt.subplots()
            ax.scatter(x,y)
            Labels = [str(i)for i in range(0,10,1)]
            for i, txt in enumerate(Labels):
                ax.annotate(txt, (x[i], y[i]))
            ax.plot([i for i in range(-100,100,1)],[i*0 for i in range(-100,100,1)],color = 'red')
            ax.plot([i*0 for i in range(-100,100,1)],[i for i in range(-100,100,1)],color = 'red')
            plt.xlim(min(-5,min(x)-5),max(+5,max(x)+5))
            ax.xaxis.set_major_locator(MaxNLocator(integer=True))
            ax.xaxis.set_minor_locator(MaxNLocator(integer=True))
            plt.ylim(min(-5,min(y)-5),max(+5,max(y)+5))
            ax.yaxis.set_major_locator(MaxNLocator(integer=True))
            ax.yaxis.set_minor_locator(MaxNLocator(integer=True))
            plt.title(instruction)
            plt.xlabel("x Position")
            plt.ylabel("y Position")
            plt.grid(True,'major','both',color='b', linestyle='-')
            plt.minorticks_on()
            plt.grid(True,'minor','both',color='r', linestyle=':')
            plt.ioff()
            plt.show()
            plt.pause(2)
            plt.close()

    if (1): ## Optional: write to file
        f = open("BDD9Pos[9].txt", "w")
        f.write(str(KnotList[9].UniqueHist).replace('], ','],\n'))
        f.close()
        ## End Trying to debug

    return len(set(tuple(row) for row in KnotList[9].History))

if __name__ == "__main__":
    KnotList = []
    KnotPosArray = []
    input = GetInput(9,False)
    input = InputProcessing(input)
    Puzz1Ans = Puzz1(input)
    print("P1Ans: ",Puzz1Ans)#, pyperclip.copy(Puzz1Ans)
    Puzz2Ans = Puzz2(input)
    print("P2Ans: ",Puzz2Ans), pyperclip.copy(Puzz2Ans)