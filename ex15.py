# Imports the argv method
from sys import argv

# Slots in the variables into script and filename, after they were
# assigned.
script, filename = argv

# Opens the file and stores it in txt
txt = open(filename)

# From the stored variable it prints out the text and the 
# contents of the file. Remember the filename and the conents
# are two different things.
print "Here's your file %r:" % filename
print txt.read()
txt.close()

# Repeating the file input. Could use this time to add another
# file to open.
print "Type the filename again:"
file_again = raw_input("> ")

# Open() gets the content of the file.
txt_again = open(file_again)

# Prints the content of the file.
print txt_again.read()
txt_again.close()

# Need to type the file name again, because an error will pop up.