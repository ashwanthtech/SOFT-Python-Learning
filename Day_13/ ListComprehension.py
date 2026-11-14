# Normal List Comprehension

numbers = [1, 2, 3, 4, 5]
squares = [x*x for x in numbers]
print(squares)

# Even Numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even = [x for x in numbers if x % 2 == 0]
print(even)

# Odd Numbers

numbers = [1, 2, 3, 4, 5, 6]
odd = [x for x in numbers if x % 2 != 0]
print(odd)

# Convert Names into Uppercase

names = ["ashwanth", "Sahal", "Maharoof"]
upper = [name.upper() for name in names]
print(upper)

# Numbers Greater Than 5

numbers = [2, 4, 6, 8, 10]
result = [x for x in numbers if x > 5]
print(result)