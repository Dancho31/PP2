# Example 1: AND (both must be True)
print(True and True)   # True
print(True and False)  # False

# Example 2: OR (at least one True)
print(True or False)   # True
print(False or False)  # False

# Example 3: NOT (opposite)
print(not True)   # False
print(not False)  # True

# Example 4: Real example
has_money = True
has_time = False
can_go = has_money and has_time
print(f"Can go shopping: {can_go}")  # False

# Example 5: Default value
name = ""
display = name or "No name"
print(display)  # No name