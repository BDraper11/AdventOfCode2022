from AoC2022 import *
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def UniqueCheck(input):
    return (len(input) == len(set(input)))

def Puzz1(input,nChar):
    for i in range((len(input)-nChar)):
        datastreamSet = input[i:(nChar+i)]
        if UniqueCheck(datastreamSet):
            return str(i+nChar)
    return "Error"
def Puzz2(input,nChar):
    Puzz2Ans = Puzz1(input,nChar)
    return Puzz2Ans

if __name__ == "__main__":
    input = GetInput(1,6)
    Puzz1Ans = Puzz1(input[0],4)
    print("P1Ans: ",Puzz1Ans), pyperclip.copy(Puzz1Ans)
    Puzz2Ans = Puzz2(input[0],14)
    print("P2Ans: ",Puzz2Ans), pyperclip.copy(Puzz2Ans)