# Loop with break statement
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break
    print(num)
# Output: 1 2

# Loop with pass statement
for num in numbers:
    if num == 3:
        pass
    print(num)
# Output: 1 2 3 4 5

# Loop with continue statement
for num in numbers:
    if num == 3:
        continue
    print(num)
# Output: 1 2 4 5

# For loop with else statement
for num in numbers:
    if num == 3:
        break
    print(num)
else:
    print("Loop completed successfully.")
# Output: 1 2

# While loop with else statement
i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1
else:
    print("Loop completed successfully.")