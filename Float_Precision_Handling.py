# 1.Rounding Floats
# Use the built-in round() function to reduce the number of decimal places.

value = 0.1 + 0.2
rounded_value = round(value, 2)
print(rounded_value)  # Output: 0.3

# 2.Formatting Floats for Display
# Limit displayed decimals without changing the underlying value.

pi = 3.1415926535
formatted_pi = f"{pi:.2f}"
print(formatted_pi)  # Output: 3.14