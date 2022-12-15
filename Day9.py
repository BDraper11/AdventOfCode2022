import sys
if sys.version_info[0] < 3 or sys.version_info[0]==3 and sys.version_info[1]<10:
    raise Exception("Must be using Python 3.10 or greater")

from math import copysign

from AoC2022 import *
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def InputProcessing(input):
    output = []
    for row in input:
        output.append([row.split()[0],int(row.split()[1])])
    return output

def MoveHead(Hcoord,Tcoord,dir,mag,Thistory):
    for step in range(int(mag)):
        match dir:
                case 'U':
                    Hcoord[1] = Hcoord[1]+1
                case 'D':
                    Hcoord[1] = Hcoord[1]-1
                case 'L':
                    Hcoord[0] = Hcoord[0]-1
                case 'R':
                    Hcoord[0] = Hcoord[0]+1
        Tcoord = MoveTail(Hcoord,Tcoord)
        Thistory.append(Tcoord[:])
    return Thistory

def MoveTail(Hcoord,Tcoord):
    offset = [a_i - b_i for a_i, b_i in zip(Hcoord, Tcoord)]
    if any(abs(x)>1 for x in offset):
        print(offset)
        if Tcoord[0]==Hcoord[0]:
            Tcoord[1] = Tcoord[1]+int(copysign(1,offset[1]))
        elif Tcoord[1]==Hcoord[1]:
            Tcoord[0] = Tcoord[0]+int(copysign(1,offset[0]))
        elif abs(offset[0])>abs(offset[1]):
            Tcoord[1] = Hcoord[1]
            Tcoord[0] = Tcoord[0]+int(copysign(1,offset[0]))
        elif abs(offset[1])>abs(offset[0]):
            Tcoord[0] = Hcoord[0]
            Tcoord[1] = Tcoord[1]+int(copysign(1,offset[1]))
        else:
            pass
    return Tcoord

def Puzz1(input):
    Thistory = []
    Hcoord = [0,0]
    Tcoord = [0,0]
    Thistory.append(Tcoord)
    for instruction in input:
        match instruction[0]:
            case 'U':
                logging.info('\t\tMove Up %s places',instruction[1])
            case 'D':
                logging.info('\t\tMove Down %s places',instruction[1])
            case 'L':
                logging.info('\t\tMove Left %s places',instruction[1])
            case 'R':
                logging.info('\t\tMove Right %s places',instruction[1])
        Thistory = MoveHead(Hcoord,Tcoord,instruction[0],instruction[1],Thistory)
    return len(set(tuple(row) for row in Thistory))
def Puzz2(input):
    return

if __name__ == "__main__":
    
    input = GetInput(9)
    input = InputProcessing(input)
    Puzz1Ans = Puzz1(input)
    print("P1Ans: ",Puzz1Ans), pyperclip.copy(Puzz1Ans)
    Puzz2Ans = Puzz2(input)
    print("P2Ans: ",Puzz2Ans), pyperclip.copy(Puzz2Ans)