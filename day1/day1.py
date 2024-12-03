# Read the numbers from the file and split them into two arrays
array1, array2 = [], []
with open('input.txt', 'r') as file:
    for line in file:
        num1, num2 = map(int, line.split())
        array1.append(num1)
        array2.append(num2)

# Sort the arrays
array1.sort()
array2.sort()

# Calculate the total of absolute differences
total = sum(abs(a - b) for a, b in zip(array1, array2))

# Print the result
print(f"Total = {total}")

