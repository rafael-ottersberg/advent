day = '21'
import numpy as np
from sympy import symbols, solve
import time

for filename in [f'test.txt', 'input.txt']:
    print('_________________' + '\n' + filename)
    with open(f'{day}/{filename}') as f:
        tot_score = 0
        tot_score_part2 = 0

        monkeys = dict()
        for line in f.readlines():
            line = line.strip('\n')
            line_items = line.split(' ')
            monkey = line_items[0][0:4]
            if len(line_items)==2:
                monkeys[monkey] = int(line_items[1])
            else:
                monkeys[monkey] = line_items[1:4]

        def calculate(monkey, monkeys):
            if type(monkeys[monkey]) != list:
                return monkeys[monkey]
            else:
                match monkeys[monkey][1]:
                    case '+':
                        return calculate(monkeys[monkey][0], monkeys) + calculate(monkeys[monkey][2], monkeys)
                    case '-':
                        return calculate(monkeys[monkey][0], monkeys) - calculate(monkeys[monkey][2], monkeys)
                    case '/':
                        return calculate(monkeys[monkey][0], monkeys) / calculate(monkeys[monkey][2], monkeys)
                    case '*':
                        return calculate(monkeys[monkey][0], monkeys) * calculate(monkeys[monkey][2], monkeys)

        res = calculate('root', monkeys)
        print(int(res))

        t1 = time.time()
        x = symbols('x')
        monkeys['humn'] = x
        monkeys['root'][1] = '-'
        #print(monkeys['root'])
        res = calculate('root', monkeys)
        print(int(solve(res,x)[0]))
        print(time.time()-t1)