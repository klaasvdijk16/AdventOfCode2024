# Part 1
import re
import itertools

def main():
    pt1('day7/input.txt')


def pt1(file):
    total = 0
    with open(file, 'r') as f:
        clean_data = []
        data = f.read().splitlines()
        data = [re.split('[: ]', l) for l in data]

        for i in data:
            i.remove('')
            i = [int(x) for x in i]
            clean_data.append(i)


    for li in clean_data:
        res = calculator(li, ['+', '*'])
        total += res
    print(total)

def calculator(l, ops):
    needed = int(l[0])
    values = l[1:]
    combi_len = len(values)-1

    op_combinations = list(itertools.combinations_with_replacement(ops, combi_len))

    for combi in op_combinations:
        equation = [x for y in zip(values, combi) for x in y] + [values[-1]]
        num1 = None
        op = None
        num2 = None
        for i in equation:
            if isinstance(i, int):
                if not num1:
                    num1 = i
                else:
                    num2 = i
                    eq_res = int(eval(f"{num1} {op} {num2}"))
                    num1 = eq_res
                    num2 = None
                    op = None
            else:
                op = i



        if num1 == needed:
            return needed
    return 0
    

if __name__ == "__main__":
    main()