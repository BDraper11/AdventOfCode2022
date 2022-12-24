class position:
    def __init__(self, posX, posY, headVisit=False, tailVisit=False):
        self.posX = posX
        self.posY = posY
        self.headVisited = headVisit
        self.tailVisited = tailVisit


def DetermineTailPosition(headPos, tailPos):
    if abs(headPos[0] - tailPos[0]) <= 1 and abs(headPos[1] - tailPos[1]) <= 1:
        return tailPos
    else:
        tailPos = [
            tailPos[0] + max(-1, min(1, headPos[0] - tailPos[0])),
            tailPos[1] + max(-1, min(1, headPos[1] - tailPos[1])),
        ]

    return tailPos


def CheckPositionArrayForPosition(positionArray, tailPos):
    for position in positionArray:
        if [position.posX, position.posY] == tailPos:
            return True

    return False


def ProcessActionFile(input):
    global benArray
    countOfPositions = 1
    positionArray = []
    ropeKnotPosition = [
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
    ]
    positionArray.append(position(0, 0, True, True))

    for line in input:
        # print("Line: %s" % line)
        line_split = line.strip().split(" ")
        moveDirection = [0, 0]
        if "R" == line_split[0]:
            moveDirection = [1, 0]
        if "L" == line_split[0]:
            moveDirection = [-1, 0]
        if "U" == line_split[0]:
            moveDirection = [0, 1]
        if "D" == line_split[0]:
            moveDirection = [0, -1]

        for i in range(int(line_split[1])):
            ropeKnotPosition[0] = [
                ropeKnotPosition[0][0] + moveDirection[0],
                ropeKnotPosition[0][1] + moveDirection[1],
            ]
            # print("Head Position: %s" % ropeKnotPosition[0])
            for i in range(1, 10):
                ropeKnotPosition[i] = DetermineTailPosition(
                    ropeKnotPosition[i - 1], ropeKnotPosition[i]
                )
                # print("Tail Position: %s" % ropeKnotPosition[i])

            if (
                CheckPositionArrayForPosition(positionArray, ropeKnotPosition[9])
                is False
            ):
                benArray.append(ropeKnotPosition[9])
                countOfPositions += 1
                positionArray.append(
                    position(
                        ropeKnotPosition[9][0], ropeKnotPosition[9][1], False, True
                    )
                )
    f = open("SMD9Pos[9].txt", "w")
    f.write(str(benArray).replace('], ','],\n'))
    f.close()

    return countOfPositions


def main():
    
    with open("Day9Input.txt", "r") as file:
        data = file.readlines()

    countOfPositions = ProcessActionFile(data)

    print("Count of Positions: %s" % countOfPositions)

benArray = []
main()