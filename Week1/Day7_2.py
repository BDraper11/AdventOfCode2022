from AoC2022 import *
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

class Directory:
    def __init__(self,Name,ParentDirPath='',Parent=None):
        self.Name = Name
        self.Parent = Parent
        self.FullPath = ParentDirPath+Name+'/'
        self.ContainedDirs = []
        self.ContainedFiles = []
        self.Size = None
    def AddFile(self,Size,Name):
        self.ContainedFiles.append(File(Size,Name))
    def AddDir(self,Name,ParentDir,Parent):
        #ParentDir = ParentDir+'/'
        self.ContainedDirs.append(Directory(Name,ParentDir,Parent))
    def GetDir(self,DirName, root=None):
        if DirName != '' and '/' in DirName:
            for dir in self.ContainedDirs:
                if dir.FullPath == DirName:
                    return dir
        else:
            for dir in self.ContainedDirs:
                if dir.Name == DirName:
                    return dir
    def CalcDirSize(self,TargetSize):
        global CandidateDirCount, CandidateDirSize, dirSizeList
        DirSize = 0
        for file in self.ContainedFiles:
            DirSize += file.Size
        for dir in self.ContainedDirs:
            DirSize += dir.CalcDirSize(TargetSize)
        self.Size = DirSize
        dirSizeList.append([DirSize,self.FullPath])
        if DirSize<=TargetSize:
            CandidateDirCount +=1
            CandidateDirSize +=DirSize
        return DirSize
    def GetSmallestDeleteCandidate(self,StorageToFind,SmallestDeleteCandidate): # Does not work - maybe try this approach again later.
        global SmallestDeleteCandidateSize
        for dir in self.ContainedDirs:
            if (dir.Size > StorageToFind) and (dir.Size<SmallestDeleteCandidateSize):
                SmallestDeleteCandidateSize = dir.GetSmallestDeleteCandidate(StorageToFind,dir)
        print (SmallestDeleteCandidate.Size)
        return SmallestDeleteCandidate.Size

class File:
    def __init__(self,Size,Name):
        self.Name = Name
        self.Size = int(Size)
        #self.Format = '.'+Name.split('.')[1]

def Puzz1(input):
    rootPath = ''
    root = Directory(rootPath)
    thisDir = root
    input = input[1:]
    for line in input:
        if '$ cd /' in line: # Don't really need this anymore.
            pass
        elif '$ cd ..' in line:
            thisDir = thisDir.Parent
        elif '$ cd ' in line:
            thisDir = thisDir.GetDir(line.split()[2]) # Need to figure out how to set the next Directory from the class.
        elif '$ ls' == line:
            pass # Do nothing with this.
        elif 'dir ' in line:
            thisLine = line.split(' ',1)
            thisDir.AddDir(thisLine[1],thisDir.FullPath,thisDir)
        elif line[0].isnumeric():
            thisLine = line.split(' ',1)
            thisDir.AddFile(thisLine[0],thisLine[1])
        else:
            print("Error: %s",line)
    TargetSize = 100000
    root.CalcDirSize(TargetSize)
    return root
def Puzz2(root,dirSizeList):
    global TotalStorageCapacity,UpdateStorageRequired
    StorageUsed = root.Size
    StorageRemaining = TotalStorageCapacity-StorageUsed
    StorageToFind = UpdateStorageRequired-StorageRemaining
    dirSizeList.sort()
    for dirSize in dirSizeList:
        if dirSize[0] > StorageToFind:
            return dirSize[0]
    #SmallestDeleteCandidate = root.GetSmallestDeleteCandidate(StorageToFind,root) # Does not work - maybe try this approach again later.
    return 'Fail'

if __name__ == "__main__":
    CandidateDirCount = 0
    CandidateDirSize = 0
    TotalStorageCapacity = 70000000
    UpdateStorageRequired = 30000000
    SmallestDeleteCandidateSize = TotalStorageCapacity
    dirSizeList = []
    input = GetInput(1,7)
    root = Puzz1(input)
    print("P1Ans: ",CandidateDirSize), pyperclip.copy(CandidateDirSize)
    
    Puzz2Ans = Puzz2(root,dirSizeList)
    print("P2Ans: ",Puzz2Ans), pyperclip.copy(Puzz2Ans)