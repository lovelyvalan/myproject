# list []

# l = list()  # list
# ls = []     # list
lt = [1, 2, ["hello", [9]], ["valan"]]
print(lt[2][0])
print(len(lt))
print(len(lt[2]))
lt[0] = 9
print(lt)
lt.append([0, 3, 4, 5])
print(lt)
# now take an lt as a object . lt[0]=9 is the member . lt.append[0,3,4,5] is an method

'''
len() --> this function returns the lenght of whatever object you pass into it
'''

'''

i = 11, 1  # this is the tuple we can't consider it as the integer data type
print(type(i))
j = i + 2  # so we cannot add or concadenate the tuple and int .And this is the Type error
print(len(i))

'''
# kandipa 11 ah iterate pannanum na we can do type convertion

k = 111
print(len(str(k)))

ls1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, ]

# pop command remove tha last value

ls1.pop()
ls1.pop()
ls1.pop()
ls1.pop(2)  # remove the value index based
ls1.remove(5)  # remove the value value based
print(ls1)

ls2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
ls2.append(('hello', 3))
print(ls2)

g = [1, 2, 3, 4, 5, 6, 6, 7]
h = g
print(h)
g.copy()
h.append(6)
print(g)
print(h)
print('==============================================')
p = [9, 8, 7, 6, 1, 2, 3, 4, 5, ]
p.sort()
print(p)

o = [1, 2, 3, 4, 5, 'hai']
o.reverse()
print(o)

i = [1, 2, 3, 4, 5, 'hai']
i.remove(5)
print(i)

u = [1, 2, 3, 4, 5, 'hai']
u.insert(6, "valan")
print(u)

y = [1, 2, 3, 4, 5, 'hai']
print(y.index(1))

t = [1, 2, 3, 4, 4, 5, 'hai']
print(t.count(4))

r = [1, 2, 3, 4, 5, 'hai']
print(r.clear())

# + operator in list

l = [1, 2, 3, 4]
k = [5, 6, 7, 8]
j = l + k
print(j)
j = j + [9, 10]
print(j + [11, 12])

