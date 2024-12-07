# Part 1
print("Part 1:\n")
array1, array2 = zip(*[map(int, line.split()) for line in open('day1/input.txt')])
total = sum(abs(a - b) for a, b in zip(sorted(array1), sorted(array2)))
print(f"Total = {total}")

# Part 2
import pandas as pd

print("Part 2:\n")
s1 = pd.Series(array1, name='s1')
s2 = pd.Series(array2)

s2_counts = s2.value_counts()

s1_s2 = pd.merge(s1, s2_counts, 'inner', left_on='s1', right_index=True)
s1_s2['product'] = s1_s2['s1'] * s1_s2['count']

print(s1_s2['product'].sum())