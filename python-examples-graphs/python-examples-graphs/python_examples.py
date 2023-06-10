# This file includes some useful pieces of python,
# with descriptions. To get full details on any of this functionality
# you should read the official Python documentation


# We already discussed lists:

l = [2,4,6,8]

# We can add to a list
l.append(12)

print("l is now: ", l) # l is now: [2, 4, 6, 8, 12]

# Or remove the last element
x = l.pop()

print("x is:", x, "and l is:", l) # x is: 12 and l is: [2, 4, 6, 8]

# We will now introduce a new way of printing, 'f strings'
# If we put 'f' at the start of a string, then write {code}, the code is executed
# and the result is printed. We can rewrite the last print as:
print(f"x is: {x} and l is: {l}") # x is: 12 and l is: [2, 4, 6, 8]

# We can also 'pop' the first element of a list:

x = l.pop(0)

print(f"x is: {x} and l is: {l}") # x is: 2 and l is: [4, 6, 8]

# We can also find out if a value is in a list:

print(f"Is 4 in l? {4 in l}. Is 10 in l? {10 in l}")

# Sometimes we do not care about the order of terms, then we can use a set

s = set([3,4,5])

# Add with 'add'

s.add(2) # s is now set([2,3,4,5])

# Remove a value with 'pop' -- note values are removed in a random order

x = s.pop() #

print(f"popped {x} from {s}") # I popped '2', you might get a different value!

# We can use dictionaries to represent maps

d = { 'A' : 2, 'B' : 3 }

# We can get all the 'keys' using keys()

print(f"The keys of 'd' are {d.keys()}") # The keys of 'd' are ['A', 'B']

# Check if a key is present with 'in'

'A' in d # is true

# And set or get a key's value with []

d['A'] = 7


# We want to be able to save and load from files
# One common format for doing this is 'JSON', which
# comes from Javascript, but looks (almost) the same
# as Python's lists and dictionaries.

# For our purposes, we first import json

import json

# Then this will let us load a JSON file:

with open('graph.json') as f:
    loaded = json.load(f)

