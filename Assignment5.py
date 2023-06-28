# Take input from user of 5 numbers and store it in a list
numbers = []
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

# 1) Calculate the sum of all the elements in the list
sum_of_numbers = sum(numbers)
print("Sum of all elements:", sum_of_numbers)

# 2) Find the smallest number
smallest_number = min(numbers)
print("Smallest number:", smallest_number)

# 3) Find the largest number
largest_number = max(numbers)
print("Largest number:", largest_number)

# 4) Display list in ascending order
ascending_order = sorted(numbers)
print("List in ascending order:", ascending_order)

# 5) Display list in descending order
descending_order = sorted(numbers, reverse=True)
print("List in descending order:", descending_order)

# 6) Convert list into Tuple
numbers_tuple = tuple(numbers)
print("List converted to tuple:", numbers_tuple)

# 7) Delete the list
del numbers
print("List deleted.")