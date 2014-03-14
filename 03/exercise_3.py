# list all character trigrams in the sentence
import re

trigrams = []
sentence = "Keep it short and simple!"

for x in xrange(len(sentence)):			# get the trigram starting at each character of the sentence
	m = re.match(r"(...)",sentence[x:])
	if m: 
		m = re.sub("\s", "_", m.group(1))		# replace whitespace by _
		trigrams.append(m)

for t in trigrams: print t