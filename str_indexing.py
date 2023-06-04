'''
a = 'lovely_valan'
print((a[7]) is (a[-5]))
print(a[1])
print(a[7])
print(a[-5])
print(id(7))
print(id(-5))
print(a[-12])


b=[1,2,3,4,5,6]
print(b[-1])
print(b[0])

d=(1,2,3,4)
print(d[0])
'''
s = 'hello_world'
print(s[4])
print(id(s))
# s[4]=d  # string object doesnot support item assignment
s = 'hell_world'
print(s[4])
print(id(s))


# Formatting # f string

nm = 'hacker'
me = f"valan is a {nm}"
print(me)

name="lovely"
age="19"
s=f"he is {name} & {age} years old"
print(s)

st1="my name is "

n = 'lovely'
m = 'valan'
b=n+m
print(b)

# old method of string formatiing
c="my name is {name} , i'm {age} years old ".format(name="sahaya",age=19)
print(c)