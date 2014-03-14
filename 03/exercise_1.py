# lists XML tags appearing in a file
import re

root = ""
tagset = set()

# extract and store in set
with open('input_ex1.txt', 'r') as f_in:
	for line in f_in:
		m = re.match(r'<([^\?/]\w*)\s*[a-zA-Z0-9="]*>',line)
		if m:
			tag = m.group(1)
			if root == "": 		# first appearing element is set as root: is parent to all other elements
				root = tag
			tagset.add(tag)		# storing XML tags in a set guarantees uniqueness

# print tags
with open('output_ex1.txt', 'w') as f_out:
	f_out.write(root + "\n\n")					# root tag with empty line
	for tag in sorted(tagset, key=str.lower):	# alphabetic list of unique tags
		f_out.write(tag + "\n")