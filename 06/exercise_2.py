# from a given list of 4 letter words, check using dictionary if changing
# one letter produces a new valid word
import copy

dictionary=set()
for word in open("output_ex1.txt", "r"):
	dictionary.add(word[:-1])

endict = [line[:-2] for line in open("english_dictionary.txt", "r") if len(line)==6] 		# 4 character words in dictionary

newwords = set()
for word in dictionary:	
	wordmatrix = [copy.deepcopy(list(word))] + [copy.deepcopy(list(word))] + [copy.deepcopy(list(word))] + [copy.deepcopy(list(word))]
	for c in xrange(ord('a'), ord('z')+1):
		for i in range(0,4):
			wordmatrix[i][i] = chr(c)
		newwords.update(set(["".join(w) for w in wordmatrix if "".join(w) in endict]))
		
dictionary.update(newwords)

with open("output_ex2.txt", "w") as f_out:
	for w in sorted(dictionary, key=str):
		f_out.write(w + "\n")