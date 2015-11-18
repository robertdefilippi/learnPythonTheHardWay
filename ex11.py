print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)
	
# The comma is at the end of lines 1 3 and 5 because the print does not end the 
# line with a newline character and go to the next line

print "Test input",
test = raw_input()

print "This was a %r test" % test

print "Another form input ... ask me something?"
test_2 = raw_input()

print "This was the second form's answer %r" % test_2
