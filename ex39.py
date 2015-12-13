stuff = {}
stuff['city'] = 'Vancouver'
stuff['country'] = 'Canada'

states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI',
}

cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville',
}

# Add more cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# Print out some cities ... notice your multiplying a string
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10

# The item() method runs through all the items in the dictionary
# Notice how state is the first category in the dict, not the result

for state, abbrev in states.items():
	print "%s is abbreciated %s" % (state, abbrev)
	
# print every city in state
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)
	
# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (
		
		# Notice how the abbrev is being called inside
		# the cities dict
		
		# cities['NY'] = 'New York'
		
		state, abbrev, cities[abbrev])
		
print '-' * 10
# safely get an abbreviation by states that might not be there
state = states.get('Texas')

# {}.get('looking for', 'return this if it does not find') 
# --> returns a value for the given key. If key is 
# not available then returns default value None.

# state in this case will be FALSE
if not state:
	print "Sorry, no Texas."
	
# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city