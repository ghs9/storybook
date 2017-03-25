# Gabriel Summers ghs9@uw.edu
# 3/8/17
# TCSS435
# Assignment 3
# storyBook.py

import random

# Global dictionary that we will use to store
# trigrams in.
GLOB_DICT = {}

# Adds all trigrams from a txt file to GLOB_DICT
def prepTrigramsFromFile(file_name):
	global GLOB_DICT
	with open(file_name) as f:
	    li =[word.lower() for line in f for word in line.split()]
	for i in range(len(li)-2):
		if li[i] in GLOB_DICT:
			if li[i+1] in GLOB_DICT[li[i]]:
				if li[i+2] in GLOB_DICT[li[i]][li[i+1]]:
					GLOB_DICT[li[i]][li[i+1]][li[i+2]] += 1
				else:
					GLOB_DICT[li[i]][li[i+1]][li[i+2]] = 1
			else:
				GLOB_DICT[li[i]][li[i+1]] = {}
				GLOB_DICT[li[i]][li[i+1]][li[i+2]] = 1
		else:
			GLOB_DICT[li[i]] = {}
			GLOB_DICT[li[i]][li[i+1]] = {}
			GLOB_DICT[li[i]][li[i+1]][li[i+2]] = 1
	f.close()

# Extracts trigrams from txt files, selects a
# random first word and prints it to an output
# file. then a random second word is chosen,
# based off of the first word. A third word
# is chosen based off of its probability of
# occuring following the second and first word.
# The printing of the second and third word is
# repeated 500 times, resulting in a story that
# is 1000 lines long.
#
# If the output file is output_complex.txt
# then all files are expected to converted
# to trigrams. If the output file is
# output_simple.txt, then all files that would
# normally be converted to trigrams should be
# commented out except for doyle-27.txt
#
# The stories do not have punctuation.
def begin():
	# output = open('output_simple.txt', 'w')
	output = open('output_complex.txt', 'w')
	# prepTrigramsFromFile('alice-27.txt')
	prepTrigramsFromFile('doyle-27.txt')
	prepTrigramsFromFile('doyle-case-27.txt')
	# prepTrigramsFromFile('london-call-27.txt')
	# prepTrigramsFromFile('melville-billy-27.txt')
	# prepTrigramsFromFile('twain-adventures-27.txt')
	firstWord = random.choice(GLOB_DICT.keys())
	# firstWord = 'The'
	output.write(''.join([firstWord,' ']))
	for i in range(500):
		secondWord = random.choice(GLOB_DICT[firstWord].keys())
		lis = []
		for word in  GLOB_DICT[firstWord][secondWord]:
			for num in range(GLOB_DICT[firstWord][secondWord][word]):
				lis.append(word)
			thirdWord = random.choice(lis)
		output.write(' '.join([secondWord,thirdWord,' ']))
		firstWord = thirdWord
	output.close()

begin()
