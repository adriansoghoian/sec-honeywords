    ## Passes in the password they want and the number of output passwords (n)
    ## N = number of desired output passwords 
    ## Pick 2 passwords individually from RockYou. 
    ## Pick another two and concatenate them
    ## Generate one toughnut
    ## Scramble all 5 passwords
    ## Put back together in a n-length list

from a import *
from toughnuts import *
from toughsalt import *
from concatenate import *
from number_suffix import *
from symbol_suffix import *

top100 = [
    '123456',
    '12345',
    '123456789',
    'password',
    'iloveyou',
    'princess',
    '1234567',
    'rockyou',
    '12345678',
    'abc123',
    'nicole',
    'daniel',
    'babygirl',
    'monkey',
    'lovely',
    'jessica',
    '654321',
    'michael',
    'ashley',
    'qwerty',
    '111111',
    'iloveu',
    '000000',
    'michelle',
    'tigger',
    'sunshine',
    'chocolate',
    'password1',
    'soccer',
    'anthony',
    'friends',
    'butterfly',
    'purple',
    'angel',
    'jordan',
    'liverpool',
    'justin',
    'loveme',
    'fuckyou',
    '123123',
    'football',
    'secret',
    'andrea',
    'carlos',
    'jennifer',
    'joshua',
    'bubbles',
    '1234567890',
    'superman',
    'hannah',
    'amanda',
    'loveyou',
    'pretty',
    'basketball',
    'andrew',
    'angels',
    'tweety',
    'flower',
    'playboy',
    'hello',
    'elizabeth',
    'hottie',
    'tinkerbell',
    'charlie',
    'samantha',
    'barbie',
    'chelsea',
    'lovers',
    'teamo',
    'jasmine',
    'brandon',
    '666666',
    'shadow',
    'melissa',
    'eminem',
    'matthew',
    'robert',
    'danielle',
    'forever',
    'family',
    'jonathan',
    '987654321',
    'computer',
    'whatever',
    'dragon',
    'vanessa',
    'cookie',
    'naruto',
    'summer',
    'sweety',
    'spongebob',
    'joseph',
    'junior',
    'softball',
    'taylor',
    'yellow',
    'daniela',
    'lauren',
    'mickey',
    'princesa']

def randomRockYouPassword():
    r = randint(0,99)
    password = top100[r]  
    return password

if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        output = []
        password0 = sys.argv[1]
        totalHoneywordNum = int(sys.argv[2])

        password1 = randomRockYouPassword()
        password2 = randomRockYouPassword()
        password3 = randomRockYouPassword() + randomRockYouPassword()
        password4 = tough_nuts().replace(' ','?') #replace the space in the toughnut

        passwords = [password0, password1, password2, password3, password4]

        for each in passwords:
            variations, password_indices = split_password(each)
            honeywords = reconstruct_honeyword(variations, password_indices, totalHoneywordNum)
            if each != password0:
                honeywords.append(each)
            output += honeywords
        shuffle(output)
        output = output[0:(totalHoneywordNum)]
        output = list(set(output)) + [ password0 ]
        shuffle(output)
        print output
    else:
        print "Pass in the password as the first command line argument and the # of honeywords as the second."
