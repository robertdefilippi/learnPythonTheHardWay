people = 5
# Creates the variables ... on all three of these lines
cats = 30
dogs = 15

if people < cats:
	print "Too many cats! The world is doomed!"
# Creates a boolean comparing the variables.
	
if people > cats:
	print "Not many cats! The world is saved!"
# Creates a boolean comparing the variables.

if people < dogs:
	print "The world is drooled on!"
	
if people > dogs:
	print "The world is dry!"
	
dogs += 5
# Adds 5 to the dogs variable
# Dogs = 20

if people >= dogs:
	print "People are greater than or equal to dogs."
# Now that dogs are +5 they want to reevaluate the variable	
# Dogs = People ... 20 = 20
	
if people <= dogs:
	print "People are less than or equal to dogs."
	
if people == dogs:
	print "People are dogs."
# The last three are are =, so the if statement will
# move to TRUE and run the print command.

# Indents need to occur because python won't run the command.
# It needs to be told there is something to run after the function
# has passed in the parameter.
	
# I want to run an 'if; with two commands

if people > cats and dogs > cats:
	print "This expression worked. True"
else:
	# Remember the colon, and to move the indent back for the
	# else statement.
	print "This expression did not work. False"
	
