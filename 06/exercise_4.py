# spellchecks using soundex "synonyms", ordered by Damereau-Levenshtein distance
import sys

# Damereau-Levenshtein distance
def dam_lev(string1, string2):
	f = [list(xrange(len(string2)+1))] 
	# construct an initial matrix adapted to the length of the strings
	for i in range(1, len(string1)+1):
		f.append([i]+[0]*len(string2))
	for (i, ci) in enumerate(string1, start=1):
		for (j, cj) in enumerate(string2, start=1):
				f[i][j] = min(f[i-1][j]+1, f[i][j-1]+1, f[i-1][j-1] + (0 if ci == cj else 1))
				# transpositions
				if i > 1 and j > 1 and ci == string2[j-2] and cj == string1[i-2]:
					f[i][j] = min(f[i][j], f[i-2][j-2] + 1)
	return f[-1][-1]

def soundex(string):
	wl = list(string.upper())
	sx = [wl[0]]
	# change letters; do not insert duplicates (pairs)
	for c in wl[1:]:
		if c in ['A', 'E', 'I', 'O', 'U', 'H', 'W', 'Y']:
			sx.append(0)
		elif c in ['B', 'F', 'P', 'V'] and sx[-1] != 1:
			sx.append(1)
		elif c in ['C', 'G', 'J', 'K', 'Q', 'S', 'X', 'Z'] and sx[-1] != 2:
			sx.append(2)
		elif c in ['D','T'] and sx[-1] != 3:
			sx.append(3)
		elif c == 'L' and sx[-1] != 4:
			sx.append(4)
		elif c in ['M','N'] and sx[-1] != 5:
			sx.append(5)
		elif c == 'R' and sx[-1] != 6:
			sx.append(6)
	sx = [str(w) for w in sx if w != 0]
	# add trailing zeros
	if len(sx) < 4:
		sx = sx + ["0"]*(4-len(sx))
	return "".join(sx[0:4])

if len(sys.argv) < 6:
	print "Proposes spelling for 5 given incorrectly spelled words."
	print "Usage example: \"python exercise_4.py hial jnea spi scaw waht\"."
else:
	dictionary = open("output_ex2.txt", "r").read().split("\n") 
	# uses the extended dictionary from ex2
	dictionary = [(word, soundex(word)) for word in dictionary[:-1]]
	for wword in sys.argv[1:6]:
		sx = soundex(wword)
		print "\nIncorrectly spelled: \"" + wword + "\", soundex: " + sx
		same_sx = [(wdict, dam_lev(wword, wdict)) for (wdict, wsoundex) in dictionary if wsoundex == sx]
		if len(same_sx) > 0:
			print "Words with same soundex code:"
			for (w, dist) in sorted(same_sx[0:5], key=lambda tup:tup[1]):
				print "\t \"" + w + "\", edit distance: " + str(dist)
		else:
			print "Sorry, unable to find corrections for " + wword + "."