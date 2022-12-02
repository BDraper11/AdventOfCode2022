import logging, sys

def GetInput(w,d):
    with open("Week"+str(w)+"\Day"+str(d)+"Input.txt") as f:
        input = f.read().splitlines()
    return input

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    logging.debug('A debug message!')
    logging.info('We processed %d records', len([1,2,3,4]))