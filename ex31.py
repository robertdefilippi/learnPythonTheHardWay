print "You are in a dark room with three doors. Do you go through door #1, #2, or #3?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your leg off. Good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
	print "Your stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"
	
elif door == "3":
	print "You arrive in a field of ice, surrounded by elves."
	print "1. Snow Elves?"
	print "2. Throw a snow ball."
	print "4. Is there a thrid option?"
	
	elf = raw_input("< ")
	
	if elf == "1":
		print "They exist! And they kill you. Good job!"
	elif elf == "2":
		print "They cast blizaga. You dead. Good job!"
	elif elf == "3":
		print "There is no three! End Game!"
	else:
		print "The 4th choice was the correct choice. Game over"
	
else:
	print "You stumble around and fall on a knife and die. Good job!"
	
# Part of the study drill is to expand the game out. I've added 
# another laying to the CYOA.