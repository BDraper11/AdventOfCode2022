import logging, sys
import pyperclip

def GetInput(w,d):
    with open("Week"+str(w)+"\Day"+str(d)+"Input.txt") as f:
        input = f.read().splitlines()
    return input

def PrintOrdtoChr(start=0,end=127):
    l = range(start,end)
    for i in l:
        print("Ord ",i,"is: ",chr(i))
if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    logging.debug('A debug message!')
    logging.info('We processed %d records', len([1,2,3,4]))