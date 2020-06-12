import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

##########THIS IS N^2 (Quadratic) runtime!##########
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

########## N log N MVP Solution ##########
#Instead we'll do N log N runtime by creating a binary tree of the first list, then checking names from the second list against it.
#grab out binary search tree node class
from binarysearch import BSTNode

# #make the root of the tree the first element in the first array
root = BSTNode(names_1[0])

# #now insert every other item in the first array to make our binary tree
for i in range(1,len(names_1)):
    root.insert(names_1[i])

#now we need to compare the second array with the tree. If there is a duplicate, we'll add it to the duplicates array
for x in names_2:
    if root.contains(x):
        duplicates.append(x)
    
########## N log N Array Stretch Solution ##########

#Sort the first array so it is in alphabetical order, according to stack overflow this is n log n https://stackoverflow.com/questions/14434490/what-is-the-complexity-of-this-python-sort-method
# names_1.sort()

# #Here's a function to see if a given word is in the sorted array

# def isDuplicate(array, value):
#     floor = 0
#     ceiling = len(array) - 1

#     while ceiling - floor > 1:
#         mid = ( ceiling - floor ) // 2 + floor
#         if value == array[mid]:
#             return True
#         if value > array[mid]:
#             floor = mid
#         elif value < array[mid]:
#             ceiling = mid
#     return False

# #okay now run the function on each item in names_2
# for x in names_2:
#     if isDuplicate(names_1, x):
#         duplicates.append(x)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

#The instructions in the readme say to only use python lists, so i'll do that above