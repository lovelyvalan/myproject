# int immutable
a = 100
print(id(a))
a = 101
print(id(a))


# List mutable

c = [1, 2, 3, ]
print(id(c))
c = [1, 2, 3, ]
print(id(c))
x = 1
print(id(x))
x = 2
print(id(x))

y = [1, 2, 3]
print(id(y))
y.append([4, 5, 6])
print(y)
print(id(y))

# STRING Immutable

s = 'hello world'
print(id(s))
#s = 'hello world '  # if variable naming format is correct then string is mutable
s.join('valan')
print(s)
print(id(s))
