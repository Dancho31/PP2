# Example 1: Skip number 3
num = 0
while num < 5:
    num += 1
    if num == 3:
        continue
    print(num)
# Output: 1 2 4 5

# Example 2: Skip even numbers
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
# Output: 1 3 5 7 9

# Example 3: Process only positives
numbers = [5, -2, 3, -1, 4]
index = 0
while index < len(numbers):
    if numbers[index] < 0:
        index += 1
        continue
    print(numbers[index])
    index += 1
# Output: 5 3 4

# Example 4: Skip specific
count = 0
while count < 6:
    count += 1
    if count == 2 or count == 4:
        continue
    print(count)
# Output: 1 3 5 6

# Example 5: Simple continue
x = 0
while x < 5:
    x += 1
    if x == 2:
        continue
    print(f"Number {x}")
# Output: Number 1, 3, 4, 5