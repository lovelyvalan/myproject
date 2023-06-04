#   dictionary {}      "" : ""

#   dictionary is not iterable / so it has no index

#   format "key " : " value"

#   key only in immutable things


"""
to do all dictionary operations  a key must be hashed .
regardless of the data type of the key it has to be hashed
"""

# create an empty dictionary
d = {}
d1 = dict()
print(type(d))
print(type(d1))

dict1 = {"name ": "sahaya", "age ": [12, 13, ], "city": "pkv", (1, 2): "hey"}
print(dict1.items())
print(dict1.keys())
print(dict1.values())
print("sahaya" in dict1)  # ------> False . in keyword only for key not for value

# in keyword .......

# In is applied for the key it can be used to check if a key is present in dictionary

ddos = {"nm": "valan", "age": 19}
print("nm" in ddos)
print("age" in ddos)
# in is only for key


# del keyword in dict

dc = {"company": "xyz", "year": 1991, "bng": 10}
# del dc["year"]
print(dc)
# other methods
print(dc.get("company"))
print(dc.items())
print(dc.keys())
print(dc.values())
dc.setdefault("year", 2021)
print(dc.items())
dc.update({"company": "valanhr","year" : 2021})
print(dc.items())
# dc.pop("year1")
dc.popitem()
print(dc.items())

print(dc.fromkeys(dc, "null", ))  # 1.sequence  # 2. value.  value is set for all the key's

dictionary = {1: "apple", 2: "orange", 3: "banana", 4: "grape", 5: "berry"}

dictionary.items()
print(dictionary.items())

print(dictionary.keys())

print(dictionary.values())

x = dictionary.copy()

print(dictionary.get(1))

dictionary.setdefault(6, "strawberry")
print(dictionary.items())
dictionary.update({4: "grapes"})
print(dictionary.items())
dictionary.pop(5)
print(dictionary.items())
dictionary.popitem()
print(dictionary.items())

# packing and unpacking

# in dictionary packing and unpacking key only returns in the given variable

df = dictionary
a, b, c, d = df
print(a)
print(b)
print(c)
print(d)

# update or adding the dictionary in existing dicctionary

d = {'a': "AAAA", 'd': "dddd"}
c = {'a': "aaaa", 'b': "bbbb", 'c': "cccc", **d}
print(c)

# dictionary topic was ended
