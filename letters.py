import string
import random

ascii_characters = list(string.ascii_uppercase + string.ascii_lowercase)
sym_letter = ["a", "A", "l", "E", "O", "o"]

def generate_strings(string):  ## output is a list of fake strings
	output = []
	while len(output) < 10:
		if len(string) > 1:
			output.append(randomize_string(string))
		else:
			output.append(randomize_letter(string))
	return [item for sublist in output for item in sublist]

def letter_to_sym(letter):
	if letter == "a":
		return "@"
	elif letter == "A":
		return "4"
	elif letter == "l":
		return "1"
	elif letter == "E":
		return "3"
	elif letter == "O":
		return "0"
	elif letter == "o":
		return "0"
	else:
		return letter

def randomize_letter(letter): # currently can generate uppercase letters too
	output = letter
	while output == letter:
		output = random.choice(ascii_characters)
	return output

def randomize_string(string):
	output = []
	string = list(string)
	temp_string = []
	output += flip_cases(string)
	while len(output) < 30:
		temp_string = string
		for i, each in enumerate(string):
			if each in sym_letter:
				if random.randrange(0,4) == 0:
					temp_string[i] = letter_to_sym(each)
		output += flip_cases(temp_string)
	return output

def flip_cases(string):
	string = list(string)
	output = []
	string_length = len(string)
	if string[0] == string[0].lower():
		output.append(string[0].upper() + "".join(string[1:]))
	while len(output) < 10:
		sample_indices = random.sample(range(len(string)), random.randrange(0,len(string)))
		for each in sorted(sample_indices):
			temp_string = string
			temp_string[each] = flip_letter_case(temp_string[each])
			output.append("".join(temp_string))
	return output

def flip_letter_case(letter):
	rand = random.randrange(0,2)
	if rand == 0:
		return letter.lower()
	else:
		return letter.upper()

if __name__ == "__main__":
	print generate_strings("adrianv")

