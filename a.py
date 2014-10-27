# Input is passed into program through the command line
import sys, string, re, copy
from letters import *
from number import *
from symbol_split import *
from random import shuffle

def split_password(string):
    password_indices = []
    output = []
    letter_search = [(m.start(0), m.end(0)) for m in re.finditer('[a-z A-Z]+', string)]
    number_search = [(m.start(0), m.end(0)) for m in re.finditer('\d+', string)]
    symbol_search = [(m.start(0), m.end(0)) for m in re.finditer('\W+', string)]
    password_indices.append(letter_search)
    password_indices.append(number_search)
    password_indices.append(symbol_search)
    output = copy.deepcopy(password_indices)
    for i, char_type in enumerate(output):
        for j, substring in enumerate(char_type):
            output[i][j] = generate_variations(string[substring[0]:substring[1]])
    return output, password_indices

def generate_variations(substring):
    try:
        int(substring[0])
        return generate_numbers(substring)
    except ValueError:
        substring[0]
    if re.match('\W+', substring):
        return switch_symbol(substring)
    else:
        return generate_strings(substring)

def reconstruct_honeyword(variations, password_indices, totalHoneywordNum): 
    start_indices = []
    for i, char_type in enumerate(password_indices):
        for j, substring in enumerate(char_type):
            start_indices.append(int(substring[0]))
    start_indices.sort()

    priority_indices = copy.copy(start_indices)
    for i, char_type in enumerate(password_indices):
        for j, substring in enumerate(char_type):
            index = start_indices.index(substring[0])
            priority_indices[index] = (i,j)
    
    output = []
    for times in range(0,totalHoneywordNum):
        psw = ''
        for pos in priority_indices:
            k = randrange(0,len(variations[pos[0]][pos[1]]))
            randString = variations[pos[0]][pos[1]][k]
            psw = psw + randString
        output.append(psw)
    return output

if __name__ == "__main__":
    if len(sys.argv) > 1:
        password = sys.argv[1]
        totalHoneywordNum = int(sys.argv[2])
        variations, password_indices = split_password(password)
        honeywords = reconstruct_honeyword(variations, password_indices, totalHoneywordNum)
        honeywords.append(password)
        shuffle(honeywords)
        print honeywords
    else:
        print "Pass in the password as the first command line argument and the # of honeywords as the second."
