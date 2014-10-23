from random import randint   

def switch_symbol(symbols):
        
    bracket_left = [40,60,91,123]
    bracket_right = [41,62,93,125]
    math = [37,43,45,47,61,92]
    punct = [34,39,44,46,58,59,95,96]
    special = [33,35,36,38,42,63]
    other = [94,124,126]
    unch = [32,64]
  
    n = 20
    new_symbols_list = []
  
    for i in range(n):
        str_len = len(symbols)
        new_symbols = ""
        for j in range(str_len):
            ascii = ord(symbols[j])    
            if ascii in bracket_left:
                length = len(bracket_left)-1
                rand = randint(0,length)
                new_ascii = bracket_left[rand]
            elif ascii in bracket_right:
                length = len(bracket_right)-1
                rand = randint(0,length)
                new_ascii = bracket_right[rand]
            elif ascii in math:
                length = len(math)-1
                rand = randint(0,length)
                new_ascii = math[rand]
            elif ascii in punct:
                length = len(punct)-1
                rand = randint(0,length)
                new_ascii = punct[rand]
            elif ascii in special:
                length = len(special)-1
                rand = randint(0,length)
                new_ascii = special[rand]
            elif ascii in other:
                length = len(other)-1
                rand = randint(0,length)
                new_ascii = other[rand]
            else:
                ascii in unch
                new_ascii = ascii     
            new_symbols = new_symbols + chr(new_ascii)
        new_symbols_list.append(new_symbols)
    print new_symbols_list
    return new_symbols_list
    