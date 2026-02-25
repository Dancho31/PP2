#1
def square_generator(n):
    for i in range(n + 1):
        yield i * i

# Test
N = int(input("Enter a number: "))
for value in square_generator(N):
    print(value)

#2
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

# Input
n = int(input("Enter a number: "))

print(",".join(str(num) for num in even_numbers(n)))

#3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Test
n = int(input("Enter a number: "))
for num in divisible_by_3_and_4(n):
    print(num)

#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

# Test
a = int(input("Enter start (a): "))
b = int(input("Enter end (b): "))

for value in squares(a, b):
    print(value)

#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

# Test
n = int(input("Enter a number: "))
for num in countdown(n):
    print(num)