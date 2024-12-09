import re

# part 1

with open('day3/input.txt') as f:
    program = f.read()

mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

mul_matches = list(re.finditer(mul_pattern, program))

total = 0
for mul in mul_matches:
    values = mul.groups()
    total += int(values[0]) * int(values[1])

print(f"result of multiplications: {total}")

# part 2

do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

do_matches = list(re.finditer(do_pattern, program))
dont_matches = list(re.finditer(dont_pattern, program))

mul_start_indices = [mul_match.start() for mul_match in mul_matches]
do_start_indices = [do_match.start() for do_match in do_matches]
dont_start_indices = [dont_match.start() for dont_match in dont_matches]

do = True
total = 0
while len(mul_matches) > 0:
    do_start_idx = do_start_indices[0] if len(do_start_indices) > 0 else 999999
    dont_start_idx = dont_start_indices[0] if len(dont_start_indices) > 0 else 999999

    possible_next_instructions = [
        mul_start_indices[0],
        do_start_idx,
        dont_start_idx
    ]

    next_instruction = possible_next_instructions.index(min(possible_next_instructions))
    if next_instruction == 0:
        mul_start_indices.pop(0)
        values = mul_matches.pop(0).groups()
        if do:
            total += int(values[0]) * int(values[1])
    elif next_instruction == 1:
        do = True
        do_start_indices.pop(0)
    else:
        do = False
        dont_start_indices.pop(0)
print(f"result of enabled multiplications: {total}")