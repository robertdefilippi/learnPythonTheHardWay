from sys import argv
# The method below shows if something is T/F
# If they exist or not.
from os.path import exists

script, from_file, to_file = argv

# print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
# I combined them on the line below. 

with open(from_file) as f:
	indata = f.read()

# in_file = open(from_file)
# indata = in_file.read()

print "Does the output file exist? %r. The input file is %d bytes long." % (exists(to_file), len(indata))

# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input()

with open(to_file, 'w') as r:
	r.write(indata)

print "Alright, all done."

r.close(); f.close()