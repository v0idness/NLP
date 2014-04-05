# counts word tokens, word types in a file
# demonstrates Zipf's law
import re
import collections

# for the plot:
import numpy as np
import matplotlib.pyplot as plt

def getwords(wl):
	wl_clean = []
	punctuation = re.compile(r'[-.?!,":;()|]')		
	for word in wl:
		w = punctuation.sub("", word).strip() 			# remove any punctuation from the word
		if re.match(r"^[a-zA-Z]",w):					# keep only real words (i.e. not numbers or starting with <)
			wl_clean.append(w)
	return wl_clean


with open("input_ex3.txt", "r") as f_in:
	tokens = getwords(re.split('(\'|\s+)', f_in.read().lower())) 	
	# split into tokens at spaces or apostrophes, unify to lowercase, then remove non-words

mostfreq = collections.Counter(tokens).most_common(100)
print "Number of word tokens: " + str(len(tokens))
print "Number of word types: " + str(len(set(tokens)))		# unique tokens
print "\nZipf's Law:"
print "Rank | Term | Expected frequency | Real frequency (both absolute)"
i = 1
c = mostfreq[0][1] 					# frequency of most frequent term as reference
for token, count in mostfreq:
	expected = 	c/i					# Zipf's law computation for rank i related to most frequent term
	separator = "\t\t" if len(token)<4 else "\t"
	print str(i) + ". " + token + separator + str(expected) + "\t" + str(count)
	i += 1

# --------------------------------
# generate log-log chart of rank/token frequencies:
plt.xlabel('rank')
plt.ylabel('frequency')
plt.title('Token frequency (top 100) in document corpus.')
plt.loglog([count for token, count in mostfreq],'bo')
plt.show()