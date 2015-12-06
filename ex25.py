# Break down each line of this code and figure out what
# it does. Also, this give the help() file a description
# of what the file does when you run it in Python.

# If you call the file ex25(break_words) and you have described
# what the function does, it will give a quick description

def break_words(stuff):
	"""This function will break up words for us."""
	# This will not show up
	"""This not will show up. Has to be in the first
	line."""
	words = stuff.split(' ')
	# Split() takes the string and breaks it into a list
	# with separate elements.
	return words
	
def sort_words(words):
	"""Sorts the words."""
	return sorted(words)
	
def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	# Pop() is removing the item at a given position in the list
	# and return it.
	print word
	
def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	# This would be the last element in the list
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns a sorted words."""
	words = break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
	
# The return from a function gives the line of code that called
# the function a result. Returning the output to the terminal.
# Print only deal with printing output to the terminal.

