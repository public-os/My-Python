# 1.Declaring Floats

# 5e3 is 5 × 10³ = 5000.0
big_number = 5e3
print(big_number)  # Output: 5000.0


# 2.Performing Basic Operations

# Adding numbers in scientific notation
result = 2e2 + 3e3  # 2×10² + 3×10³ = 200 + 3000 = 3200
print(result)       # Output: 3200.0


# 3.Rounding and Precision

precise_num = 2.34567e2   # 2.34567 × 10² = 234.567
rounded_num = round(precise_num, 2) #  Use the `round()` function to control decimal places after calculations.
print(rounded_num)        # Output: 234.57

# 4.Formatting Output

large_value = 1234567890
formatted_value = f"{large_value:.3e}" # `:.3e` specifies scientific notation with three decimals.
print(formatted_value)  # Output: 1.235e+09

distance = 1234567890.0
print(f"{distance:.2e} kilometers")