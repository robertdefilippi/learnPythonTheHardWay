i = 0
numbers = []
numbers_2 = []

# i starts at zero and continues until 5
while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
	
	# The total will go over 5, and up to 6 because
	# this happens inside the loop.
	i += 1
	
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i

# This print is outside the while loop	
print "The numbers: "

# Runs a loop through the array
# creates a new line every time an element is called
for num in numbers:
	print num

# Rewrite this using a FOR loop

def second_time(r, k):
	'''r is the loops, k is the increment'''
	n = 0
	for q in range(0, r):
		print "At the top n is %d." % n
		numbers_2.append(n)
	
		n += k
	
		print "Numbers now: ", numbers_2
		print "At the bottom q is %d." % n
	
		if n >= r:
		
			print "The numbers: "
		
			for num in numbers_2:
				print num

second_time(3,4)

print range(0,10,3)
# [0, 3, 6, 9]
