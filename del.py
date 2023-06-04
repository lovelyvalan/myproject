# CURD operation  is a mastered in doing these on a data
# C -> create
# U -> update / edit
# R -> read
# D -> delete

# if you can do this curd operation on a data you'll become a master in programming

# del is a keyword that delete an item or variable whatever you declared it will be undeclared or deleted

a = [1, 2, 3, [4, 5, 6], 7, 8, 9, ]
a.remove(9)
print(a)
del a[5]

# del   remove()   .clear

l = list(range(0, 100))

l.remove(99)    # remove only the defined value
del l[5]        # remove the value assigned in the given index value
l.clear()       # clear all the data's inside the list
del l           # delete the l variable


c =[ 1,2,3]
c.pop()      # empty pop remove the last value
c.pop(1)     # if i give index value of the c it will remove specified index value
print(c)

