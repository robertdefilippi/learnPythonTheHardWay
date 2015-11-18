tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# The \t is a tab
# The \n is a new line
# The \\ allows for a backslash to appear

# Let's try '''

var_test = '''Test
Test
Test 
'''

print var_test

# Maybe ''' is not used and """ is used, is because the double quotes
# are easier to see?

a = 'a'
b = 'b'
c = 'c'

print """
Let's %s,
If this %s works out
As well as I %s I think it will
""" % (a, b, c)

# Always remember this, r is for debugging and s is for displaying
