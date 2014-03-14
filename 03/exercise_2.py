# XML format validator
# takes filename as command line argument
import re
import sys

format = True 		# initially assume no violation
root = "" 			# empty root element
root_closed = False
tag_stack = []		# tags should follow a stack (LIFO) in order to be nested properly
errors = set()		# all errors encountered in the file (each message only once)


# extract and store in set
with open(sys.argv[1], 'r') as f_in:
	for line in f_in:
		if re.search(r"\s*<[^?/]",line):			# opening tag except for xml version tag
			if root_closed:							# if there is another element after the root closed
				format = False
				errors.add("root element not enclosing all elements")

			tag = re.split('\s+', re.search(r"<([^/][^>]*)>",line).group(1)) 	# split into name and attributes
			if len(root) == 0: 				# set first tag as root element
				root = tag[0]
			tag_stack.append(tag[0])		# push tag name to stack
			if re.match(r"^([\d\-:\.]|xml)",tag[0],re.I) or re.search(r"[!\"#$%&'()*+,/;<=>?@\[\\\]^`{|}~]",tag[0]):
				format = False
				errors.add("tag naming error")
			if len(tag) > 1:				# if there are attributes
				for attribute in tag[1:]:
					if not re.match(r"\w*=([\"][^\"]*[\"]|[\'][^\']*[\'])",attribute):
						format = False
						errors.add("tag attribute format error (not correctly enclosed in quotes)")
			

		if re.search(r"</",line):			# closing tag
			tag = re.search(r"</([^>]*)>",line).group(1)
			if tag == root:
				root_closed = True
			if tag == tag_stack[-1]: 		# if tag is the uppermost on the stack
				tag_stack.pop()
			elif tag.lower() == tag_stack[-1].lower():
				tag_stack.pop()				# pop anyway - otherwise obviously also displays nesting errors
				format = False
				errors.add("tags are case sensitive")
			else:
				format = False
				errors.add("tag nesting error")


if len(tag_stack) > 0:			# if some tag was not popped from the stack
	errors.add("not all tags were closed")


print "Is", sys.argv[1], "well formed?", "YES" if format else "NO, errors:"
if len(errors) > 0:
	for e in errors:
		print e