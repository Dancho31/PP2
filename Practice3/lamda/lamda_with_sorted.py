students = [("Ann", 22), ("John", 18), ("Mike", 25)]

sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)