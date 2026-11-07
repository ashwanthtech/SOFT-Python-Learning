# Tuple
fruits = ("Apple", "Mango", "Orange")
print(fruits)

# Access Tuple Elements
days = ("Monday", "Tuesday", "Wednesday")
print(days[0])
print(days[1])
print(days[2])

# Find Tuple Length
numbers = (10, 20, 30, 40, 50)
print(len(numbers))

# Loop Through a Tuple
fruits = ("Apple", "Mango", "Orange")
for x in fruits:
    print(x)

# Check an Element
fruits = ("Apple", "Mango", "Orange")

if "Mango" in fruits:
    print("Mango is available")
else:
    print("Not available")

# Tuple Cannot Be Changed
days = ("Monday", "Tuesday", "Wednesday")
print(days[0])

# Simple Tuple Mini Program
students = ("Ashwanth", "Anila", "Shabu")
print("Student Names:")
for name in students:
    print(name)
print("Total Students:", len(students))