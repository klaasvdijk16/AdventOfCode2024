import numpy as np

rules = []
updates = []

with open('day5/input.txt') as f:
    readRules = True
    for line in f:
        if line == '\n':
            readRules = False
        elif readRules:
            rules.append([int(x) for x in line.rstrip().split('|')])
        else:
            updates.append([int(x) for x in line.rstrip().split(',')])

rules = np.array(rules)
updates = np.array(updates, dtype=object)
left_rules = np.array([rule[0] for rule in rules])
right_rules = np.array([rule[1] for rule in rules])

# part 1

incorrect_updates = []
total = 0
for update in updates:
    correct_update = True
    for idx, page in enumerate(update):
        pages_that_may_not_occur_left = right_rules[np.where(left_rules == page)]
        pages_that_may_not_occur_right = left_rules[np.where(right_rules == page)]
        if (np.any(np.isin(pages_that_may_not_occur_left, update[:idx], assume_unique=True)) or
            np.any(np.isin(pages_that_may_not_occur_right, update[idx+1:], assume_unique=True))
        ):
            correct_update = False
            break
    if correct_update:
        total += update[len(update) // 2]
    else:
        incorrect_updates.append(update) # prep for part 2
print(f"Sum of middle page numbers of correctly-ordered updates: {total}")

# part 2

total = 0
for update in incorrect_updates:
    applicable_rules = []
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            applicable_rules.append(rule)
    errors = 9999
    while errors != 0:
        errors = 0
        for rule in applicable_rules:
            if update.index(rule[0]) > update.index(rule[1]):
                errors += 1
                update.remove(rule[0])
                update.insert(update.index(rule[1]), rule[0])
    total += update[len(update) // 2]
    
print(f"Sum of middle page numbers of fixed incorrectly-ordered updates: {total}")
