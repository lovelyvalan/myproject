# SET {} is an valueless dictionary
# set values are only immutable
# set is mutable
# set na tamil la kanam . serppu kanam antha  madiri ellam

s = set()
print(type(s))

s1 = {1,2,3,4,4,4}
print(s1)


set1 =  {1,2,3,4,5}

set2 =  {5,6,7,8,9}

print(set1 & set2) # intersection. &  -> ambrocent
print(set1 | set2) # union. | -> name is pipe
print(set1 - set2) # difference
print(set2 - set1) # difference
print(set1 ^ set2) # asymmetric

# other methods

a = {1,2,3,4,5,7,8}
b = {1,2,3,6}
a.add(6)
print(a)

c = a
a=c.copy()
c.add(7)
print(c)
print(a)

d={7,8,6,9}

print(a.union(b))
(a.remove(4))
print(a)
print(a.issuperset(b))    # if values of a exist in b then  a is superset
print(a>=b)               # >= is superset
print(b.issubset(a))      # if values of b is
print(b<=a)               # < is subset
print(a.isdisjoint(d))
print(d.pop())
print(d)
print(d <= a )             # all the values in d contains same in a is superset or subset.
# extra values not problem but must same value if exist then <= , >= is possible

(d.update(a))
print(a)
print(d)
