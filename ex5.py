name = 'Robert R. F. DeFilippi'
age = 29
height = 74.0 # inches
in_to_m = 0.0254
height_m = height * in_to_m
weight = 200.0 # lbs
lb_to_kg = 0.453592
weight_kg = weight * lb_to_kg
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %r m tall." % height_m
print "He's %d pounds heavy." % weight
print "He's %r kg heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# Use %r to pass exactly what you want into the "print" command.
# The % .... will convert the value into what is shown next to the %.
# Such as they will convert a float into an integer.