# For Loop (A for loop repeats code for each item in a sequence)

for i in range(1, 6):
    print(i)

# Print fruits (Example for loop)

fruits = ["Apple", "Mango", "Orange"]
for fruit in fruits:
    print(fruit)

# While Loop (Print numbers from 1 to 5)

i = 1
while i <= 5:
    print(i)
    i = i + 1

# Break Statement (break stops the loop)

for i in range(1, 6):
    if i == 4:
        break
    print(i)

# Continue Statement (continue skips the current iteration)
for i in range(1, 6):
    if i == 3:
        continue
    print(i)