# Creates a clean exit from the program
from sys import exit

# Defining all the functions upfront (top) of the code
# so that the main function can be read below

def gold_room():

	print "This room is full of gold. How much do you take?"
	
	choice = raw_input("> ")
	
	if "0" in choice or "1" in choice:
		# Passes the string input into how_much
		# as an int to the var below

		# Odd command as only 0 or 1 allow you to get the
		# correct answer.

		how_much = int(choice)
	
	else:
		# dead() is def below
		dead("Man, learn to type a number.")
		
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	
	else:
	# Exits you from the stream
		dead("You greedy bastard! You die trying to carry it all")
		
def bear_room():
	
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"

	# Declaring this now, because it will be modified below
	# to be T or F

	bear_moved = False
	
	# This creates an infinite loop
	while True:
		choice = raw_input("> ")
		
		if choice == "take honey":
		
			dead("The bear looks at you then slaps your face off.")
			# Notice how when this is called, it returns this string
			# as well as "good job"
		
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		
		elif choice == "open door" and bear_moved:
			# Calling the function to make sure
			gold_room()
		
		else:
		# Loops until an exit for different function is called
			print "I have no idea what that means."

def cthulhu_room():
	
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever ...  stares at you and you go insane."
	print "Do you flee for your life or eat your own head?"
	
	choice = raw_input("> ")
	
	# Notice there is no "while True" loop
	# But it keeps looping.
	
	if "flee" in choice:
		start()
	
	elif "head" in choice:
		dead("Well that was tasty!")
	
	else:
		cthulhu_room()
		
def dead(why):
	
	print why, "Good job!"
	# Passes the param "why" and then prints both
	# Asks python to leave the system, and stop the program
	exit(0)
	
def start():
	
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	choice = raw_input("> ")
	
	if choice == "left":
		bear_room()
	
	elif choice == "right":
		cthulhu_room()
	
	else:
		dead("You stumble around the room until you starve.")

# Calls the function to start		
start()