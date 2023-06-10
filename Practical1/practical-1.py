# Insert your code here
# You can edit and change this part any way you like,
# including adding new functions and classes

def friendlypartcount(n):
    print("TODO: Implement friendlypartcount")
    return 0
    
def friendlypartlist(n):
    print("TODO: Implement friendlypartlist")
    return [ ]


#############################################################################
# Testing code, please do not change code under here.
# Except to comment out lines which your code cannot correctly execute
#############################################################################


print("The number of friendly partitions of 5 is:", friendlypartcount(5))
print("The number of friendly partitions of 12 is:", friendlypartcount(12))
print("The number of friendly partitions of 50 is:", friendlypartcount(50))
print("The number of friendly partitions of 500 is:", friendlypartcount(500))

print("A full list of the friendly partitions of 12 is:")

val = friendlypartlist(12)

# some simple checks
if len(val) != friendlypartcount(12):
    print("Oh no! friendlypartcount(12) is ", friendlypartcount(12))
    print("But, the length of friendlypartlist(12) is ", len(val))

for l in val:
    if not sorted(l):
        print("Oh no! ", l, " was not sorted")
    if not sum(l)==12:
        print("Oh no!", l, " does not add up to 12")

print(val)




