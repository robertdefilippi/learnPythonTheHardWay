# This is a string separated by spaces. But it is still one string.
ten_things = "Apples Oranges Crows Telephone Light Sugar"
# "Apples Oranges Crows Telephone Light Sugar"

# print(ten_things)
# 42

print "Wait ... there are NOT 10 things in that list. Let's fix that."

# This springs the string into sperate elements in a list.
stuff = ten_things.split(' ')
# ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar']

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# print len(stuff)
# 6

# Notice how the len of the array is the elements in the array
# while the len of the string is the entire length of the string (# of char).

# The length of stuff
while len(stuff) != 10:
	
	# pop() removes and returns the last element of the list
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	# Because the pop() returns the last element, you can show which one is being added
	# to the list
	
	# The append() adds an item to the list "stuff"
	stuff.append(next_one)
	
	# Now we know how long the new (append(ed)) string is
	print "There are %d items now." % len(stuff)
	

# The indent shows the while loop is done. Prints it all off.
print "There we go: ", stuff

print "Let's do some things with stuff."

# Prints the first element
print stuff[1]

# prints the LAST element
print stuff[-1] # whoa! fancy

# Takes the FINAL element, removes it from a list, and returns it.
print stuff.pop()

# Joins every element of a list or a string with the characters before the 
# dot operator.
print ' ' .join(stuff) #what? cool!

# Joins the 3rd and 4th elements of 'stuff' with '#'
print '#'.join(stuff[3:5]) # Super stellar!
# Telephone#Light

# more_stuff.pop() is the same as pop(more_stuff)

# Study Drills

# 6. What are 10 things which would work in a list?
# Cards, Types of Food, Number of Fingers, Items in a Store, Fruit in a Basket,
# Keys on a Board, Threads in a Sweater, Cars on a Bridge, Stars in the Sky, Houses
# on a Street.

