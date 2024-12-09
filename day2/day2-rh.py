import itertools

def is_safe_report(report: list) -> bool:
    safe_report = True
    increasing = None
    for i in range(len(report)-1):
        left = report[0+i]
        right = report[1+i]
        if i != 0 and increasing and right - left <= 0:
            safe_report = False
            break
        elif i != 0 and not increasing and right - left >= 0:
            safe_report = False
            break
        elif abs(right - left) > 3 or right == left:
            safe_report = False
            break
        increasing = True if right > left else False
    return safe_report

# part 1

reports = []
with open('day2/input.txt') as f:
    for report in f.readlines():
        reports.append([int(x) for x in report.split()])

n_safe_reports = 0
for report in reports.copy():
    if is_safe_report(report):
        reports.remove(report)
        n_safe_reports += 1

print(f"Number of safe reports: {n_safe_reports}")

# part 2

for report in reports:
    permutations = list(itertools.combinations(report, len(report)-1))

    safe_report = False
    for perm in permutations:
        if is_safe_report(perm):
            safe_report = True
            break
    if safe_report:
        n_safe_reports += 1

print(f"Number of tolerant safe reports: {n_safe_reports}")
