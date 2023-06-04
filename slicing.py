# iterable
#  means is traversable/index
# if it has index then slicing is possible


# var[index]  ===>returns a  value      -->  common for all
# var[start:stop-1:step] ===>  returns a list/collection   ---> only in pyhton

# step is always 1 if is not mentioned
l = [1, 2, 3, 4, 5, 6, 7, 8]
print(l[2:5:1])  # this is same to below
print(l[2:5])  # this is same to above

ls = 'lovely valan'
print(ls[7:])

# i'll be right back
# its mutable immutable content
# print(id(ls))

n = [1, 2, 3]
m = n
print(id(n))
print(id(m))
m = n.copy()
print(id(n))
print(id(m))
m = n[::1]
print(id(n))
print(id(m))

# shadow copy ngurathu list ka id ah mattum tha change pannum sublist/nested list id ah change pannathu

import copy

# shallow copy

s = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12, ]]
d = s
print(s)
print(d)
d = copy.copy(s)
print(id(s))  # main list id mattum change aagum
print(id(d))
print(id(s[0]))  # sublist id same ah tha irukum,
print(id(d[0]))

s[0][2] = 4
print(s)

# deepcopy
f = s
f = copy.deepcopy(s)
print(id(f))  # main list id um different ah irukum
print(id(s))
print(id(s[0]))  # sublist id um differnet ah irukum
print(id(f[0]))
print("======================")
print(id(f[3]))
print(id(s[3]))
print("======================")
f[3].extend([13, 14, 15])  # only modification will be considered in copy function
# otherwise normally adding elements is won't change the deepcopy or shallow copy
print(f[3])
print(s[3])
print(f)
print(s)

"""
print(s[::1])
print(s[1:4:1])

"""

# deepcopy

c = [1, 2, 3], [4, 5, 6], [7, 8, 9]
v = c
print(id(c))
print(id(v))
v = copy.deepcopy(c)
print(id(c))
print(id(v))
c[2].append([10, 11, 12])  # here append can append int items but multiple int assigned here so it's now tuple
print(c),print(type(c))
print(v)


# deepcopy

# here copy () function do deepcopy
# without using copy module normal copy is done by j=h[::1]

h =[[1,2,3,[4,5,6]]]
j = h
j = h.copy()
j[0][3]=[7,8,9]
print(j)
print(h)
"""
# normal copy

j = [1,2,3]
k = j
k = j[::1]
k.append([4,5,6])
print(k)
print(j)
"""

# return back to slicing

# syntax [start : stop : step]

l = list(range(0,101))
print(l)
print(l[101:0:-2])
print(l[101:48:-2])
print(l[0:52:2])
print(l[0:32:4])

s="valav"
if s[::-1] == s[::1]:
    print(
        "this is a palindrom"
    )
else:
    print(
        "this is not an palindrom"
    )
