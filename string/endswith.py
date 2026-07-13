# string.endswith(suffix, start, end)

text = "Hello, world!"
print(text.endswith("world!"))  # Output: True
print(text.endswith("Hello"))   # Output: False

# Using start and end parameters
print(text.endswith("lo", 0, 5))     # Output: True (checks the substring "Hello")
print(text.endswith("world", 0, 12)) # Output: True (checks "Hello, world")