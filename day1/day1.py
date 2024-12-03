
array1, array2 = zip(*[map(int, line.split()) for line in open('input.txt')])
total = sum(abs(a - b) for a, b in zip(sorted(array1), sorted(array2)))
print(f"Total = {total}")
