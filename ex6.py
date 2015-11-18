# Passes in 10 to the % operator
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# Passes in binary and do_not into the string below
y = "Those who knew %s and those who %s." % (binary, do_not)

print x
print y

# The string below has a double % pass through with x and 10. Line 2 and line 12
print "I said: %r." % x
# This has a triple % pass through, with y, binary, and do_not
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# Uses a boolean as a pass through for %. And, it works.
print joke_evaluation % hilarious

# Adds two strings together.
w = "This is the left side of..."
e = "a string with a right side."

print w + e