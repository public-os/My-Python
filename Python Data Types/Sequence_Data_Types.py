# Sequence Data Types
# A sequence is an ordered collection of items,
# which can be of similar or different data types.
# Elements in a sequence can be accessed using indexing.

# 1.String
s = 'Welcome to the Geeks World'
print(s)
print(type(s))

# access string with index
print(s[1])
print(s[-1])

# 2.List
a = [1, 2, 3]
print(a)

b = ["Geeks", "For", "Geeks", 4, 5]
print(b[3])
print(b[-3])

# 3.Tuple
t1 = (1,)
print(type(t1))

t2 = ('Geeks', 'For', 'Geeks', 1, 2)
print(t2[3])
print(t2[-3])