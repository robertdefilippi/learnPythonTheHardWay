# This one is like your scripts with args
# The * puts the params into a list which can be distributed
# just like below.
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r,arg2: %r" % (arg1, arg2)
	
# This just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1
	
# This one takes no argument
def print_none():
	print "I got nothin'."
	
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

# Notice we need to define a function using def
# This is different from javascript where you need to
# write out function() {}; UGH!