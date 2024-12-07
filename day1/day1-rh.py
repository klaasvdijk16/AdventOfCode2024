import numpy as np

left, right = np.split(np.sort(np.loadtxt('day1/input.txt').T).flatten(), 2)
total = int(np.sum(np.abs(left - right)))
print(f"Total = {total}")

similarity_score = int(np.sum(left * np.array([np.count_nonzero(right == i) for i in left])))
print(f"Similarity score = {similarity_score}")
