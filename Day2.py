from AoC2022 import *
'''
Puzz1 Rules
Rock        A   X
Paper       B   Y
Scissors    C   Z

Scoring:
Rock        1
Paper       2
Scissors    3
-------------
Win     6
Draw    3
Loss    0

Per contest need:
+ Result score
+ Shape score
+ Round score

Puzz2 Rules
X   Lose
Y   Draw
Z   Win
'''
def CalcResultScore(line):
    AwinDict = {
        "X":3,
        "Y":6,
        "Z":0
    }
    BwinDict = {
        "X":0,
        "Y":3,
        "Z":6
    }
    CwinDict = {
        "X":6,
        "Y":0,
        "Z":3
    }
    DictOfWinDicts = {
        "A":AwinDict,
        "B":BwinDict,
        "C":CwinDict
    }

    #print(line[0],",",line[-1])
    #print(DictOfWinDicts[line[0]][line[-1]])
    return DictOfWinDicts[line[0]][line[-1]]
def CalcShapeScore(line):
    ShapeScoreDict = {
        "X":1,
        "Y":2,
        "Z":3
    }
    return ShapeScoreDict[line[-1]]
def Puzz1(input):
    ResultScore = []
    ShapeScore = []
    RoundScore = []
    for line in input:
        ResultScore.append(CalcResultScore(line))
        ShapeScore.append(CalcShapeScore(line))
        RoundScore.append(CalcResultScore(line)+CalcShapeScore(line))
    TotalScore = sum(RoundScore)
    return TotalScore
def CalcResultScore2(line):
    ResultScoreDict = {
        "X":0,
        "Y":3,
        "Z":6
    }
    return ResultScoreDict[line[-1]]
def CalcShapeScore2(line):
    AshapeDict = {
        "X":3,
        "Y":1,
        "Z":2
    }
    BshapeDict = {
        "X":1,
        "Y":2,
        "Z":3
    }
    CshapeDict = {
        "X":2,
        "Y":3,
        "Z":1
    }
    DictOfShapeDicts = {
        "A":AshapeDict,
        "B":BshapeDict,
        "C":CshapeDict
}
    return DictOfShapeDicts[line[0]][line[-1]]
def Puzz2(input):
    ResultScore = []
    ShapeScore = []
    RoundScore = []
    for line in input:
        ResultScore.append(CalcResultScore2(line))
        ShapeScore.append(CalcShapeScore2(line))
        RoundScore.append(CalcResultScore2(line)+CalcShapeScore2(line))
    TotalScore = sum(RoundScore)
    return TotalScore
if __name__ == "__main__":
    input = GetInput(1,2)
    print("P1Ans: ",Puzz1(input))
    print("P2Ans: ",Puzz2(input))