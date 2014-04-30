# extract 4 letter words into a dictionary file
import re

def getwordset(wl):
	wl_clean = set()
	punctuation = re.compile(r'[-.?!,":;()|]')		
	for word in wl:
		w = punctuation.sub(" ", word).strip() 			# remove any punctuation from the word
		if re.match(r"[a-zA-Z]{4}$",w):	# keep only real words (i.e. not numbers or starting with <) of at least 3 characters
			wl_clean.add(w)
	return wl_clean

dictionary = sorted(getwordset(re.split('(\s+|,|-)', open("input_ex1.txt", "r").read().lower())), key=str) 	# split into tokens at spaces, unify to lowercase, then remove non-words using getwords

with open("output_ex1.txt", "w") as f_out:
	for w in dictionary:
		f_out.write(w + "\n")