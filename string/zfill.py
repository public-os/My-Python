# string.zfill(width)

number = "42"
padded_number = number.zfill(5)
print(padded_number) # Output: 00042
# "42" becomes "00042", ensuring a length of 5 by adding leading zeros.

negative_number = "-5"
padded_negative = negative_number.zfill(4)
print(padded_negative) # Output: -005 
# "-5" becomes "-005", ensuring a length of 4 by adding zeros in between '-' and '5'.