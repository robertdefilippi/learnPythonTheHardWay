the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list

for number in the_count:
	print "This is count %d" % number
	
# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it

for i in change:
	print "I got %r" % i

# We can also build lists, first start with an empty one
# I'm using this empty list (below) as a base for
# what I'm going to be building later.
elements = []

# Then use the range function to do 0 to 5 counts
# because the range is 0 to n-1
for i in range(0, 6):
	print "Adding %d to the lists." % i
	# append is a function that lists understand
	# Add an item to the end of the list
	elements.append(i)
	
# now we can print them out too
# in the step above we added items to elements list
for i in elements:
	print "Element was: %d" % i
	if i == 5:
		print elements

# How would you avoid the for loop for i in range(0, 6)?
element_2 = range(0,10); print element_2
# And I did it on one line :D

# In the 5th position, insert -2
element_2.insert(5,-2)

# In the -2nd position, insert 5
element_2.insert(-2,5)
print element_2
# [0, 1, 2, 3, 4, -2, 5, 6, 7, 5, 8, 9]