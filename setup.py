# Input is passed into program through the command line
import sys, string, re, copy
from letters import *
from number import *
from symbol_split import *

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

def reconstruct_honeyword(variations, password_indices):
	for i, char_type in enumerate(password_indices):
		for j, substring in enumerate(char_type):

if __name__ == "__main__":
	if len(sys.argv) == 2:
		password = sys.argv[1]
	else:
		print "Please pass in a password as a command line argument, please."
	variations, password_indices = split_password(password)
	print password_indices
