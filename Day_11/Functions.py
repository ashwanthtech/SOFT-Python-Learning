# Simple Function

def greet():
    print("Hello World!")
greet()

# Function with Parameters

def add(a, b):
    print(a + b)
add(10, 20)

# Function with Return

def multiply(a, b):
    return a * b
result = multiply(5, 4)
print(result)

# Function to Find Square

def square(num):
    return num * num
print(square(5))
print(square(10))

# Function with If-Else

def check_number(num):
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
check_number(10)
check_number(7)

# Function with Default Parameter

def greet(name="Student"):
    print("Hello", name)
greet()
greet("Ashwanth")