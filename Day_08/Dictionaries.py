# Creating a dictionary

student = {
    "name": "Ashwanth",
    "age": 18,
    "course": "Python",
    "mark": 90
}

print(student)


#Accessing dictionary values

student = {
    "name": "Ashwanth",
    "age": 18,
    "mark": 90
}

print(student["name"])
print(student["age"])
print(student["mark"])


#Adding a new item

student = {
    "name": "Ashwanth",
    "age": 18
}

student["course"] = "Python"

print(student)

#Updating a value

student = {
    "name": "Ashwanth",
    "age": 18
}

student["age"] = 19

print(student)

#Removing an item

student = {
    "name": "Ashwanth",
    "age": 18,
    "mark": 90
}

student.pop("age")

print(student)

#Using a for loop in a dictionary

student = {
    "name": "Ashwanth",
    "age": 18,
    "mark": 90
}

for key, value in student.items():
    print(key, ":", value)

#Checking whether a key exists

student = {
    "name": "Ashwanth",
    "age": 18
}

if "name" in student:
    print("Name exists")
else:
    print("Name not found")