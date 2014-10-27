import re
import copy
import sys
from random import randrange
from random import random
from math import log

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
    i = randrange(1,shift)
    shiftedPattern = ''
    for c in pattern:
        newC = chr(ord(c)+i)
        shiftedPattern += (newC)
    result = n.replace(pattern,shiftedPattern)
    
    return result

def matchSequential(n):
    matchPatternList = []

    for length in range(10,3,-1):
        for start in range(0,11-length):
            sample = ""
            for i in range (0,length):
                sample = sample + str(start+i) 
            matchPatternList.append(sample)
            matchPatternList.append(sample[::-1])
    
    for matchPattern in matchPatternList:
        if n.find(matchPattern) > -1:
            patternExist = True
            return [matchPattern, patternExist]
    return ['',False]

def ifMatchSequential(n):
    p1 = 0.33
    p2 = 0.1
    p3 = 0.57
    p = random()
    
    [matchPattern, patternExist] = matchSequential(n)
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
    result = [False, n]

    pattern1 = r"19\d{2}[0-1]\d[0-3]\d"
    pattern2 = r"[0-1]\d[0-3]\d19\d{2}"
    pattern3 = r"19\d{2}"
    randYear = str(randrange(1940,1999))
    randMonth = str(randrange(101,113))[1:]
    randDay = str(randrange(101,130))[1:]

    if re.search(pattern1, n, flags = 0):
        newN = re.sub(pattern1 ,randYear+randMonth+randDay,n)
        return [True, newN]
    elif re.search(pattern2, n, flags = 0):
        newN = re.sub(pattern2,randMonth+randDay+randYear,n)
        return [True, newN]
    elif re.search(pattern3, n, flags = 0):
        newN = re.sub(pattern3,randYear,n)
        return [True, newN]
    return result

def randomnize(string):
    n = int(string)
    for i in range(0,3):
        salt = randrange(1,int(n))
        n = log(n + salt)
    newN = str(n).replace('.','')[0:len(string)]
    return newN

def generate_numbers(string):
    output = []
    [matchPattern, patternExist] = matchSequential(string)
    birthdayExist = ifMatchBirthday(string)[0]
    
    if len(string) == 1:
        for i in range(0,iter_times):
            output.append(str(randrange(0,9)))
        return output

    if patternExist and birthdayExist:
        for i in range(0,iter_times):
            output.append(ifMatchBirthday(string)[1])

        for j,item in enumerate(output):
            output[j] = (ifMatchSequential(item))
    elif birthdayExist and not patternExist:
        for i in range(0,iter_times):
            output.append(ifMatchBirthday(string)[1])
    elif patternExist and not birthdayExist:
        for i in range(0,iter_times):
            output.append(ifMatchSequential(string))
    else:
        for i in range(0,iter_times):
            output.append(randomnize(string))

    return output

if __name__ == "__main__":

    sampleN = '191'
    if len(sys.argv) > 1:
        sampleN = sys.argv[1]
    print generate_numbers(sampleN)
