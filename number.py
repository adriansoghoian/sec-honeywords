import re
import copy
import sys
from random import randrange
from random import random

iter_times = 100

def flipSequential(n,pattern):
    reversedPattern = pattern[::-1]
    result = n.replace(pattern,reversedPattern)
    return result

def appendSequential(n,pattern):
    randNum = randrange(0,9)
    appendedPattern = pattern + str(randNum)
    result = n.replace(pattern,appendedPattern)
    return result

def shiftSequential(n,pattern):
    shift = min(9 - int(pattern[-1]), 9 - int(pattern[0]))
    i = randrange(0,shift)
    shiftedPattern = ''
    for c in pattern:
        newC = chr(ord(c)+i)
        shiftedPattern += (newC)
    result = n.replace(pattern,shiftedPattern)
    
    return result

def matchSequential(n):
    #TODO matchPatternList
    matchPatternList = ["123456","4321",'12345','23456']
    
    for matchPattern in matchPatternList:
        if n.find(matchPattern) > -1:
            patternExist = True
            return [matchPattern, patternExist]
        else:
            patternExist = False
            return [matchPattern, patternExist]
    return ['',False]

def ifMatchSequential(n):
    p1 = 0.33
    p2 = 0.1
    p3 = 0.57
    p = random()
    #flip
    newN = n
    [matchPattern, patternExist] = matchSequential(n)
    if patternExist:
        if p < p1:
            #print 'flipping'
            newN = flipSequential(n,matchPattern)
        elif p < p1 + p2:
            #print 'appending'
            newN = appendSequential(n,matchPattern) 
        else:
            #print 'shifting'
            newN = shiftSequential(n,matchPattern)
    return newN

def ifMatchBirthday(n):
    randYear = str(randrange(1940,1999))
    randMonth = str(randrange(101,113))[1:]
    randDay = str(randrange(101,130))[1:]
    #n = re.sub(r"19\d{2}",randYear,n)
    newN = re.sub(r"19\d{2}[0-1]\d[0-3]\d",randYear+randMonth+randDay,n)
    newN = re.sub(r"[0-1]\d[0-3]\d19\d{2}",randMonth+randDay+randYear,newN)
    newN = re.sub(r"19\d{2}",randYear,newN)
    
    return newN

def generate_numbers(string):
    output = []
    [matchPattern, patternExist] = matchSequential(string)
    
    if len(string) == 1:
        for i in range(0,iter_times):
            output.append(str(randrange(0,9)))
    elif patternExist:
        for i in range(0,iter_times/2):
            output.append(ifMatchBirthday(string))
            print ifMatchBirthday(string)

        output1 = copy.deepcopy(output)
        for item in output1:
            output.append(ifMatchSequential(item))
    else:
        for i in range(0,iter_times):
            output.append(ifMatchBirthday(string))
    #TODO IF MATCH BIRTHDAY PATTERN, ELSE

    return output

if __name__ == "__main__":

    sampleN = '19630722123456'
    if len(sys.argv) > 1:
        sampleN = sys.argv[1]
    print generate_numbers(sampleN)
