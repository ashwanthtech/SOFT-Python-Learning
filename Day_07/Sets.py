# 1. Create a Set

fruits = {"apple", "banana", "orange", "mango"}
print(fruits)

#2. Add an Element

fruits = {"apple", "banana", "orange"}
fruits.add("mango")
print(fruits)

#3. Remove an Element

fruits = {"apple", "banana", "orange"}
fruits.remove("banana")
print(fruits)

#4. Find the Length of a Set

numbers = {10, 20, 30, 40, 50}
print(len(numbers))

#5. Set Does Not Allow Duplicates

numbers = {10, 20, 30, 20, 10}
print(numbers)

#6. Union and Intersection

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Union:", A | B)
print("Intersection:", A & B)