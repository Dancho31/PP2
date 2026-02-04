# Example 1: Count 1 to 3
count = 1
while count <= 3:
    print(count)
    count += 1
# Output: 1 2 3

# Example 2: Count down
num = 5
while num > 0:
    print(num)
    num -= 1
# Output: 5 4 3 2 1

# Example 3: Sum numbers
total = 0
n = 1
while n <= 5:
    total += n
    n += 1
print(f"Total: {total}")  # 15

# Example 4: Until condition
password = ""
while password != "1234":
    password = "1234"
print("Logged in")  # Prints once

# Example 5: Simple loop
i = 0
while i < 3:
    print("Hello")
    i += 1
# Output: Hello Hello Hello