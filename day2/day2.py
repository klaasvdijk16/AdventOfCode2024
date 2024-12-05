total = 0

with open('input.txt', 'r') as file:
    for line in file:
        report = [int(num) for num in line.split()]

        differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
        
        ascending = True
        for diff in differences:
            if diff <= 0 or diff > 3:
                ascending = False
                break

        descending = True
        if not ascending:
            for diff in differences:
                if diff >= 0 or diff < -3:
                    descending = False
                    break

        if ascending or descending:
            total += 1

print(total)
