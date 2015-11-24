from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If your don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# Line prompts you to act, but really it is just a 
# break in the code so you opt out if need be.
raw_input("?")

print "Opening the file..."
# The 'w' is so you can write in the file
target = open(filename, 'w')

print "Trucating the file. Goodbye!"
# This is the code that deletes your file.
# Does this right now. So say goodbye to your code.
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file."

# This writes directly in the file.
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()

# Remember to close the file so you save memory.