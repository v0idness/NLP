# counts all bigrams in a file
# takes as command line argument the threshold for bigrams to be stored in the output
import re
import collections
import sys

def getwords(wl):
	wl_clean = []
	punctuation = re.compile(r'[-.?!,":;()|]')		
	for word in wl:
		w = punctuation.sub("", word).strip() 			# remove any punctuation from the word
		if re.match(r"^[a-zA-Z]",w):					# keep only real words (i.e. not numbers or starting with <)
			wl_clean.append(w)
	return wl_clean

def bigrams(words):
    prev = None				# first bigram will be (None, firstword)
    for w in words:
        yield (prev, w)
        prev = w

with open("input_ex4.txt", "r") as f_in:
	wordlist = getwords(re.split('\s+', f_in.read().lower())) 		# split into words at spaces, unify to lowercase, then remove non-words
	bigrams = bigrams(wordlist)			# convert list of words into generator of all existing bigrams

with open("output_ex4.txt", "w") as f_out:
	count = collections.Counter(bigrams)
	for bigram in [(bigram, c) for bigram, c in count.most_common() if count[bigram] > int(sys.argv[1])]:
		f_out.write(str(bigram) + "\n")