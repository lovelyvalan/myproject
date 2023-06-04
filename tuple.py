# TUPLES ()

# tuple are immutable list

# CURD ---> mutable , C & R ----> immutable

# tuples only can do C and R  in CURD. create and update only possible. update /edit or delete not possible

# tuple single value must be ended with comma
t1 = tuple((1, [3, 4]))
t1[1].append(5)
print(type(t1))
print(t1)
t1[1].remove(4)
print(t1)

# empty tuple
t = (())
print(type(t))

# packing and unpacking works as lists and tuple
# Type 1

y = 1, 2, 3  # ---> `packing
print(type(y))
a, b, c = y  # ---> unpacking
print(a)
print(b)
print(c)

# Type 2

z = 1, 2, 3, 4, 5
*a, b, c = z  # when variables and values are not equal then apply this * to a,b,c whatever you want
print(a)
print(b)
print(c)  # here c conatains last 3 vales as a list

# Type 3  # swapping

a = 1,
b = 3,
print(type(a))
print(type(b))
a, b = (b, a)

print(a)
print(b)

# + operator in tuple

t = (1, 2, 3)
print(type(t))
tp = t + (4, 5)
print(tp + (6,) + (7, 8))  # here 6 is without comma considered as a int


# comma seperated values becoming a tuple is called packing
n = 1, 2, 3, 4
print(type(n))

a =1
b =2
c=a
a=b
b=c
print(a)
print(b)