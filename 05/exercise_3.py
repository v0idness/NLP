# insert words into dictionary, count collisions
import re

def fnv1(input):
	hashed = 2166136261
	for c in input:
 		hashed = hashed * 16777619
 		hashed = hashed ^ ord(c)
 		hashed = hashed % (2 ** 32)
	return hashed

def getwords(wl):
	wl_clean = []
	punctuation = re.compile(r'[-.?!,":;()|]')		
	for word in wl:
		w = punctuation.sub(" ", word).strip() 			# remove any punctuation from the word
		if re.match(r"[a-zA-Z][a-zA-Z][a-zA-Z]+",w):	# keep only real words (i.e. not numbers or starting with <) of at least 3 characters
			wl_clean.append(w)
	return wl_clean

class Dictionary:
	def __init__(self, cap):
		self.dictionary = [None]*cap

	def incCap(self):
		self.dictionary = self.dictionary + [None]*len(self.dictionary)

	def insert(self, string):
		for i in [entry for entry in self.dictionary if entry != None]: 						# string already present somewhere in dictionary
			if string in i:
				raise Exception("String already present:", string)
		index = fnv1(string)%len(self.dictionary)
		if self.dictionary[index] != None: 			# collision: same index, different string
			if type(self.dictionary[index]) is list:	
		 		self.dictionary[index].append(string)
		 	else:  
		 		self.dictionary[index] = [self.dictionary[index], string]
		else: 										# new index
			self.dictionary[index] = string
		if len([entry for entry in self.dictionary if entry != None]) >= 2 * len(self.dictionary) / 3:
			self.incCap()

	def remove(self, string):
		found = False
		for i in [entry for entry in self.dictionary if entry != None]: 
			if string in i:
				found = True
				if type(i) is list:
					for w in i: 					# remove from collision list
						if w == string:
							i.remove(w)
				else:
					for x in range(0,len(self.dictionary)):
						if self.dictionary[x] == string:
							self.dictionary[x] = None
							break
		if not found:
			raise Exception("String not in dictionary:", string)

	def lookUp(self, string):
		return string if string in self.dictionary else "NULL"

	def size(self):
		return len([entry for entry in self.dictionary if entry != None and entry != []])

	def capacity(self):
		return len(self.dictionary)

	def sumCollisions(self): 								# sum of the lengths of collision lists
		collisions = [len(entrylist) for entrylist in self.dictionary if type(entrylist) is list and len(entrylist) > 1]
		return sum(collisions) if len(collisions) > 0 else "no hash collisions in corpus"

	def maxCollisions(self): 								# max length of entry in collision list
		collisions = [len(entrylist) for entrylist in self.dictionary if type(entrylist) is list]
		return max(collisions) if len(collisions) > 0 else "no hash collisions in corpus"

# ----- read and store into dictionary
with open("input_ex3.txt", "r") as f_in:
	tokens = getwords(re.split('(\'|\s+|,|-)', f_in.read().lower())) 	# split into tokens at spaces or apostrophes, unify to lowercase, then remove non-words using getwords

dictionary = Dictionary(1000)

for t in tokens:
	try:
		dictionary.insert(t)
	except Exception:
		pass

with open("output_ex3.txt", "w") as f_out:
	f_out.write("Total number of collisions: " + str(dictionary.sumCollisions()))
	f_out.write("\nMaximum number of collisions per index: " + str(dictionary.maxCollisions()))
	f_out.write("\nFinal size: " + str(dictionary.size()))
	f_out.write("\nFinal capacity: " + str(dictionary.capacity()))