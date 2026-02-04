# Example 1: Stop at 5
count = 1
while count <= 10:
    print(count)
    if count == 5:
        break
    count += 1
# Output: 1 2 3 4 5

# Example 2: Find number
num = 1
while True:
    if num == 7:
        print("Found 7")
        break
    num += 1
# Prints: Found 7

# Example 3: Password attempt
attempt = 1
while attempt <= 5:
    if attempt == 3:
        print("Access granted")
        break
    attempt += 1

# Example 4: Until sum > 10
total = 0
i = 1
while i <= 10:
    total += i
    if total > 15:
        break
    i += 1
print(f"Stopped at {i}")

# Example 5: Simple break
x = 0
while x < 100:
    print(x)
    if x == 3:
        break
    x += 1
# Output: 0 1 2 3