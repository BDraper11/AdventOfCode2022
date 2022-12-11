from AoC2022 import *
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

class dir:
    def __init__():
        return

def DetDirectoryList(input):
    LastCDCount = 0
    NextCDCount = 0
    ListCount = 0
    DirCount = 0
    FileCount = 0
    dirPathList = []
    dirDepthList = []
    dirContentsList = []
    dirDepth = 0
    for line in input:
        if '$ cd /' in line:
            dirDepth = 0
            CurrentPath = '/'
            dirPathList.append(CurrentPath)
        elif '$ cd ..' in line:
            LastCDCount +=1
            dirDepth -=1
            CurrentPath = ('/').join(CurrentPath.split('/')[:-2])+'/'
        elif '$ cd ' in line:
            NextCDCount +=1
            dirDepth +=1
            CurrentPath = CurrentPath+line[5:]+'/'
        elif '$ ls' == line:
            ListCount +=1
        elif 'dir ' in line:
            thisLine = line.split(' ')
            dirPathList.append(CurrentPath)
            dirDepthList.append([dirDepth])
            contents.extend(thisLine)
            dirContentsList.append(contents)
            DirCount +=1
        elif line[0].isnumeric():
            thisLine = line.split(' ',1)
            contents = [CurrentPath]
            contents.extend([dirDepth])
            contents.extend(thisLine)
            dirContentsList.append(contents)
            FileCount +=1
        else:
            print("Error: %s",line)
    return dirContentsList


def Puzz1(input):
    paths = []
    for element in input:
        paths.append(element[0])
    paths = list(set(paths))
    for path in paths:
        for element in input:
            pass
    return paths
def Puzz2(input):
    return

if __name__ == "__main__":
    input = GetInput(1,7)
    DirectoryList = DetDirectoryList(input)
    Puzz1Ans = Puzz1(DirectoryList)
    #print("P1Ans: ",Puzz1Ans), pyperclip.copy(Puzz1Ans)
    #Puzz2Ans = Puzz2(input)
    #print("P2Ans: ",Puzz2Ans), pyperclip.copy(Puzz2Ans)