# Rules for if statements
# 1 Every if must have an else
# 2 Use else functions with a die to find errors
# 3 Never nest ifs two deep just one
# 4 Treat ifs like paragraphs where else if elif else is like sentence
# Put blank lines before and after
# 5 Have simple boolean test. If complex, calculate outside 

# Rules for loops
# 1 Do not use a "debugger"
# 2 The best way to debug a program is to use "print" to
# print out the values at points in the program to see
# where they go wrong
# 3 Do not write massive fules of code. Write a little. Run.
# Fix. Repeat.

# Write something similar to the last exercise

# How to create software:

# 1 List the things you want to accomplish in this task
# 2 Pick the easiest thing you can do from your list
# 3 Write out English comments in your source file as a guide for
# how you would accomplish this task
# 4 Write some of the code under the comments
# 5 Run the script to see if it works
# 6 Write-Test-Fix-Next, cycle
# 7 Pick the next task and go for it

from sys import exit

sprung = 0

def dead(reason):
	print reason, "You're dead!"
	exit(0)

def head_back():

	print "You are BACK in a room with two doors. Why did you do that?"
	print "You still need to pick a door to go through"
	
	start_choice = raw_input("> ")
	
	if start_choice is "1":
		room_1()
	
	elif start_choice is "2":
		room_2()
		
	else:
		# Runs both without getting into an infinite loop
		choose(); start()

def choose():

	print "Choose again"

def room_1():
		
	if sprung == 0:
		trap()
	
	else:
	
		print "You made it to room 1!"
		print "If you want to exit the game now, just exit."

		room2_action = raw_input("> ")
	
		while True:
			if room2_action == "exit":
				# Remember to put exit(0) when calling exit
				print "Bye!"
				exit(0)
			
			elif room2_action == "back":
				head_back()
	
			else:
				print "Don't you want to exit???"
				room_1()

def room_2():

	print "You made it to room 2! Amazing"
	print "You see a arcade cabinat. What do you do?"
	arcade_action = raw_input("> ")
	
	# Notice how it needs to be case sensitive
	if arcade_action == "play":
		dead("You play until you're dead.")
		
	elif arcade_action == "back":
		head_back()
			
	else:
		print "You need to keep playing!"
		room_2()

def trap():
	
	# Brining down the global variable so it can be
	# modified
	global sprung
	sprung =+ 1

	print "On the way to Room 1 you see hole in the ground."
	print "It has a string coming out of it."
	print "What do you do?"
	
	trap_action = raw_input("> ")
	
	if trap_action == "touch":
		print "You should not have touched it."
		dead("Boom!")
		
	
	else:
		print "You avoid the trap"
		room_1()
	

def start():

	print "You are in a room with two doors"
	print "You need to pick a door to go through"
	
	start_choice = raw_input("> ")
	
	if start_choice is "1":
		room_1()
	
	elif start_choice is "2":
		room_2()
		
	else:
		# Runs both without getting into an infinite loop
		choose(); start()

start()

