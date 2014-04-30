# spellchecks for missing or switched characters
import sys
import re

def missingLetter(string):
	corrections = set()
	for i in range (0,len(string)+1):
		wl = list(string)
		wl.insert(i, ".")
		wre = re.compile('%s' % "".join(wl))	
		for dword in dictionary:
			if re.match(wre, dword):
				corrections.add(dword)
	return corrections

def interchanged(string):
	corrections = set()
	for i in range(0,len(string)-1):
		new = switch(string, i)
		if new in dictionary:
			corrections.add(new)
	return corrections

def switch(string, pos): 	
	wl = list(string)
	wl[pos], wl[pos+1] = wl[pos+1], wl[pos]
	return "".join(wl)

def spellcheck(string):
	a = missingLetter(string)
	b = interchanged(string)
	a.update(b)
	return list(a)

if len(sys.argv) < 2:
	print "Wrong number of command line arguments given. Usage: \"python exercise_3.py word\" where word is to be spellchecked."
else:
	dictionary = open("output_ex2.txt", "r").read().split("\n")
	word = sys.argv[1]
	if word in dictionary:
		print "Correctly spelled."
	else:
		corrections = spellcheck(word)
		if len(corrections) > 0:
			print "Suggestions:" 
			for new in sorted(corrections, key=str):
				print new
		else:
			print "No corrections found."