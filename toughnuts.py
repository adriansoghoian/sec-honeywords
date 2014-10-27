from random import randint

def tough_nuts():
    """
    returns toughnut honeyword
    """   
    lower_case = range(97, 123)
    upper_case = range(65, 91)
    numbers = range(48, 58)
    symbols = [40,41,60,62,91,93,123,125,37,43,45,47,61,92,34,39,44,46,58,59,63,95,32,33,35,36,38,42,63,94,124,126,64]
  
    toughnut = []
    n = 16
    entropy = randint(n,n*2)
    for i in range(entropy):
        rand_list = randint(1,4)
        if rand_list == 1:
            length = len(lower_case)-1
            rand = randint(1,length)
            char = chr(lower_case[rand])
            toughnut.append(char)
        elif rand_list == 2:
            length = len(upper_case)-1
            rand = randint(1,length)
            char = chr(upper_case[rand])
            toughnut.append(char)
        elif rand_list == 3:
            length = len(numbers)-1
            rand = randint(1,length)
            char = chr(numbers[rand])
            toughnut.append(char)
        else:
            length = len(symbols)-1
            rand = randint(1,length)
            char = chr(symbols[rand])
            toughnut.append(char)
    toughnut = ''.join(toughnut)
    return toughnut
    
    
#print tough_nuts()
         
