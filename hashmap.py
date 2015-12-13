from types import StringType

def new(num_buckets=256):
	
	"""Initializes a Map with the given number of buckets."""
	
	aMap = []
	for i in range(0, num_buckets):
	
		# You're creating 256 empty lists inside aMap
		aMap.append([])
	
	return aMap

def hash_key(aMap, key):
	
	"""Given a key this will create a number and then convert it 
	to an index for the aMap's buckets.
	It is creating an uniquie key for every instance of Key.	
	"""	
	
	return hash(key) % len(aMap)

def get_bucket(aMap, key):
	
	"""Given a key, find the bucket where it would go.
	The "Key" is whatever you define it as.
	Not necessarily the State, Abbrev, or City"""
	
	bucket_id = hash_key(aMap, key)
	
	return aMap[bucket_id]

def get_slot(aMap, key, default=None):
	
	"""
	Returns the index, key, and a value of a slot found in a bucket.
	Returns -1, key, and default (None if not set) when not found.
	"""
	
	bucket = get_bucket(aMap, key)
	
	# enumerate(sequence, start = 0)
	# puts numbers next to all 'sequence'
	# list(enumerate(NAME OF THING))
	
	for i, kv in enumerate(bucket):
		
		# kv equals your dict keys
		
		k, v = kv
		
		# this unpacks the kv tuple into individual elements
		
		if key == k:
			
			return i, k, v
	
	return -1, key, default
	
def get(aMap, key, default=None):
	
	"""Gets the value in a bucket for the given key, or the default.
	There is a default for abbrev, which is 'None' """
	
	assert type(key) is StringType, "key is not a string: %r" % key
	i, k, v = get_slot(aMap, key, default=default)
	
	return v
	
def set(aMap, key, value):
	
	"""Sets the key to the value, replacing any existing value."""
	
	bucket = get_bucket(aMap, key)
	
	i, k, v = get_slot(aMap, key)
	
	if i >= 0:
		
		# the key exists, replace it
		bucket[i] = (key, value)
	
	else:
	
		# the key does not exist, append to create it
		bucket.append((key, value))

def delete(aMao, key):

	"""Deletes the given key from the Map."""

	bucket = get_bucket(aMap, key)
	
	for i in xrange(len(bucket)):

		k, v = bucket[i]
		if key == k:
	
			del bucket[i]
			# Breaks out of the for loop
			break
		
def list(aMap):
	"""Prints out what's in the Map."""
	
	for bucket in aMap:
	
		if bucket: 
			
			for k, v in bucket:
	
				print k, v
				
# Adding explanation of assert()

# ASSERT == "This should never occur in reality, and if it does, we give up"
# You want to crash the program early so that you can find errors

# assert Thing that would be true, "Print this if not %" % r

# assert only appears if the thing printed out was incorrect

# There are also some extra assert cases below.
# https://pymbook.readthedocs.org/en/latest/testing.html

def dump(aMap):
	"""Dumps the completed dictionary so you can alayize it"""
	
	return aMap

# collections.OrderedDict()
# different ways to order a dictionary: value, string length, key alphabetically 
