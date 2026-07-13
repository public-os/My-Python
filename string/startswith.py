item_code = "item-bookOfKnowledge"

# Check if the item code starts with "item-" and if the rest is in title case
is_valid_prefix = item_code.startswith("item-")
is_valid_lower_case = item_code[5:].islower()  # Checking if part after 'item-' is in lower case

# Print the results separately
print(is_valid_prefix)
print(is_valid_lower_case)