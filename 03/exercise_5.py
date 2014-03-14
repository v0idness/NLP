# prints context of n words around the searchterm: ...(n words) France (n words)...
# takes as command line argument the number of words to be considered as context
import re
import sys

searchterm = "France"

def getwords(lwl):
	lwl_clean = []
	punctuation = re.compile(r'[-?!,":;()|]')
	for wl in lwl:
		wl_clean = []		
		for word in wl:
			w = punctuation.sub("", word).strip() 			# remove any punctuation from the word
			if re.match(r"^[a-zA-Z]",w):					# keep only real words (i.e. not numbers or starting with <)
				wl_clean.append(w)
		lwl_clean.append(wl_clean)
	return lwl_clean			# "cleaned" list of word lists

def getcontext(n,listlist):
	ncontexts = []
	for l in listlist:
		indices = [i for i,word in enumerate(l) if word.lower() == searchterm.lower()] 		# get all occurrences - case-insensitive - of the searchterm in a sentence
		for i in indices:
			lower = i-n if i>=n else 0
			upper = i+n+1 			# upper bound of indices doesn't matter; no "array out of bound"
			ncontexts.append(l[lower:upper])
	return ncontexts

with open("input_ex4.txt", "r") as f_in:
	contexts = re.split("\.", f_in.read())			# split contexts at dots
	words = [re.split("\s+", context) for context in contexts]		# split each context into words (splits at spaces, newline, tabs, ...)
	words = getwords(words)							# remove non-words and punctuation
	termcontexts = getcontext(int(sys.argv[1]),words)

with open("output_ex5.txt", "w") as f_out:
	for context in termcontexts:
		f_out.write(str(context) + "\n")