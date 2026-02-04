# Example 1: True or False from numbers
print(bool(5))   # True
print(bool(0))   # False

# Example 2: Empty things are False
print(bool(""))      # False
print(bool([]))      # False
print(bool([1,2]))   # True

# Example 3: In if statement
money = 100
if money:
    print("You have money")   # This prints
else:
    print("No money")

# Example 4: Check if list has items
my_list = []
if my_list:
    print("List has items")
else:
    print("List is empty")    # This prints

# Example 5: Simple bool()
print(f"bool(10) is {bool(10)}")   # True
print(f"bool(None) is {bool(None)}")  # False