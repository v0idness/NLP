# hashed dictionary implementation
def fnv1(input):
	hashed = 2166136261
	for c in input:
 		hashed = hashed * 16777619
 		hashed = hashed ^ ord(c)
 		hashed = hashed % (2 ** 32)
	return hashed

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

# ------- a couple of tests
dictionary = Dictionary(3)
try:
	dictionary.insert("creamwove") 				# these two strings collide with FNV according to
	dictionary.insert("quists")					# http://programmers.stackexchange.com/questions/49550/which-hashing-algorithm-is-best-for-uniqueness-and-speed
except Exception as e:
	print e
try:
	dictionary.insert("test")
except Exception as e:
	print e
print dictionary.lookUp("test")
try:
	dictionary.remove("test")
except Exception as e:
	print e
print dictionary.lookUp("test")
print dictionary.size()
print dictionary.capacity()