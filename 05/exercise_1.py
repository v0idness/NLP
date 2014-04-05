# FNV-1 hash implementation

def fnv1(input): 					# 32 bit version
	hash = 2166136261
	for c in input:
 		hash = hash * 16777619
 		hash = hash ^ ord(c)
 		hash = hash % (2 ** 32) 	# shorten to 32 bit
	return hash

print('Enter what you would like to hash:') 
tohash = raw_input()
print fnv1(tohash)