from sys import argv

# Puts the inputs into the var
script, input_file = argv

# Prints the input
def print_all(f):
	print f.read()
	
# The seek() function finds the "byte" you want to start at
def rewind(f):
	f.seek(0)
	
def print_a_line(line_count, f):
	print line_count, f.readline()
	
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)