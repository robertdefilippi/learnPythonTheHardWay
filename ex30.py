people = 30
cars = 40
trucks = 155555

if cars > people:
	print "We should take the cars."
	
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."
	
if trucks > cars:
	print "That's too many cars."
elif trucks < cars:
	print "Maybe we could take the trucks."
else:
	print "We still can't decide."
# The elif sets up the if to have a else built in
# so the program knows there is going to be switch coming up.

# If the variable people is greater than trucks, do this
# Else do this.
if people > trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."
	
# Here is some complex boolean expression
if people < trucks or trucks > cars:
	print "Test out how these works."
else:
	print "Test!!!"
	
