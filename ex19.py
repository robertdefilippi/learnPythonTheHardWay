# This is a simple function with two params as the inputs

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %r cheese!" % cheese_count
	print "You have %r boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# Use int() to change the raw input to int not strings.
print "Or, we can use variables from our script. \nLets get an input."
amount_of_cheese = int(raw_input("How much cheese do you want? < "))
amount_of_crackers = int(raw_input("How many crackers do you want? < "))

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# You can do math in the params before it is run by the function.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


