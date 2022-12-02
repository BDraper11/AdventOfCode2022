def GetInput():
    with open("Week1\Day1Input.txt") as f:
        input = f.read().splitlines()
        #print(str(len(input[0]))+"/t"+str(2**12))
    return input