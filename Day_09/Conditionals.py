# If statement

age = 18
if age >= 18:
    print("You are eligible to vote")

# If-Else statement

number = 7
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# If-Elif-Else statement

mark = 85
if mark >= 90:
    print("Grade A")
elif mark >= 75:
    print("Grade B")
elif mark >= 50:
    print("Grade C")
else:
    print("Failed")

# Nested If statement

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Entry not allowed")

# Check Positive or Negative

number = -5
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")