# Example 1: Stop at 5
for i in range(10):
    if i == 5:
        break
    print(i)
# Output: 0 1 2 3 4

# Example 2: Find item
items = ["pen", "book", "phone", "laptop"]
for item in items:
    if item == "phone":
        print("Found phone!")
        break
    print(f"Looking for phone, found {item}")
# Output: Looking for phone, found pen/book, Found phone!

# Example 3: Stop when sum > 10
total = 0
for i in range(1, 10):
    total += i
    if total > 15:
        break
print(f"Stopped at {i}")

# Example 4: Simple break
for x in [1, 2, 3, 4, 5]:
    print(x)
    if x == 3:
        break
# Output: 1 2 3

# Example 5: Break in loop
for num in [2, 4, 6, 7, 8]:
    if num % 2 != 0:  # if odd
        print(f"Found odd: {num}")
        break
    print(num)
# Output: 2 4 6 Found odd: 7