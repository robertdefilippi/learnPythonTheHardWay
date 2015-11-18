formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

# The string above has both " and ' inside the string
# This can be done because it takes the first used quote
# and runs until the quote is closed.

# The formatter was put inside the formatter by ...
# calling the formatter on itself. Kinda like x += x 