## Calculate top 4 closest passwords in rockyou using the text similarity library
## Scramble these 4 along with the original passwords
## Output n strings (depending on the user input)

import sys, random
import jellyfish as jf
from sets import Set
from a import *
import random

def load_pws_in_memory(txt_file_path):
	passwords = []
	for i, line in enumerate(file(txt_file_path)):
		row = line.split()
		try:
			passwords.append(row[1])
		except IndexError:
			True
	return passwords

def find_similar_pws(pw, pw_list, num_passwords):
	match_indices = []
	best_leven_distances = []
	distance = 0
	for i, each in enumerate(pw_list):
		distance = jf.levenshtein_distance(pw, each)
		match_indices.append(i)
		best_leven_distances.append(distance)
	pwd_tuples = sorted(zip(match_indices, best_leven_distances), key=lambda tup: tup[1])
	pwd_tuples = pwd_tuples[2000:100000]
	pwd_tuples = [ pwd_tuples[i] for i in sorted(random.sample(xrange(len(pwd_tuples)), 1000)) ]
	output = lookup_pwds(pwd_tuples, pw_list, num_passwords)
	return output

def lookup_pwds(tuples, pw_list, num_passwords): 
	count = 0
	output = []
	for i, each in enumerate(tuples):
		if pw_list[ each[0] ] not in output:
			output.append(pw_list[ each[0] ])
			count += 1
		if count == num_passwords:
			break
	return output

if __name__ == "__main__":

	if len(sys.argv) > 1:
		output = []
		password = sys.argv[1]
		totalHoneywordNum = int(sys.argv[2])
		passwords = load_pws_in_memory("rockyou-withcount.txt")
		passwords = find_similar_pws(password, passwords, 4) + [ password ]
		for each in passwords:
			variations, password_indices = split_password(each)
			honeywords = reconstruct_honeyword(variations, password_indices, totalHoneywordNum)
			if each != password:
				honeywords.append(each)
			output += honeywords
		shuffle(output)
		output = output[0:(totalHoneywordNum)]
		output = list(set(output)) + [ password ]
		shuffle(output)
		print output
		print len(output)
	else:
		print "Pass in the password as the first command line argument and the # of honeywords as the second."
