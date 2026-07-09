# 1. Letters and Numbers Only
print("Hello123".isalnum())  # Output: True
#  Every character is a letter or a digit, so `isalnum()` returns `True`

# 2. Space Included  
print("Hello 123".isalnum())  # Output: False
# The space disqualifies the string from being alphanumeric.

# 3. Special Characters
print("Hello!".isalnum())     # Output: False
# The exclamation mark (`!`) is not alphanumeric.

# 4. Empty String  
print("".isalnum())           # Output: False
# An empty string does not meet the alphanumeric criteria, so the method returns `False`.