# Example 1: Grade system
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")   # Prints this
elif score >= 70:
    print("C")
else:
    print("F")

# Example 2: Time of day
hour = 14
if hour < 12:
    print("Morning")
elif hour < 18:
    print("Afternoon")  # Prints this
else:
    print("Evening")

# Example 3: Number check
num = 0
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")   # Prints this

# Example 4: Age group
age = 25
if age < 13:
    print("Child")
elif age < 20:
    print("Teen")
else:
    print("Adult")   # Prints this

# Example 5: Size check
size = "M"
if size == "S":
    print("Small")
elif size == "M":
    print("Medium")  # Prints this
elif size == "L":
    print("Large")
else:
    print("Unknown")