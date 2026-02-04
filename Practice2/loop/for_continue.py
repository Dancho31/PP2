# Example 1: Skip number 3
for i in range(5):
    if i == 3:
        continue
    print(i)
# Output: 0 1 2 4

# Example 2: Skip vowels
word = "hello"
for letter in word:
    if letter in "aeiou":
        continue
    print(letter)
# Output: h l l

# Example 3: Only even numbers
for i in range(10):
    if i % 2 != 0:
        continue
    print(i)
# Output: 0 2 4 6 8

# Example 4: Skip empty
items = ["cat", "", "dog", "", "bird"]
for item in items:
    if item == "":
        continue
    print(item)
# Output: cat dog bird

# Example 5: Simple continue
for x in [1, 2, 3, 4, 5]:
    if x == 2:
        continue
    print(x)
# Output: 1 3 4 5