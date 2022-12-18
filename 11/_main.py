day = '11'
import numpy as np
import copy

for filename in [f'test.txt', 'input.txt']:
    print('_________________' + '\n' + filename)
    with open(f'{day}/{filename}') as f:
        monkeys = dict()
        for i, line in enumerate(f.readlines()):
            line = line.strip('\n')

            line_nr = ((i+1) % 7)

            match line_nr:
                case 1:
                    monkey = int(line.split(' ')[1].strip(':'))
                    monkeys[monkey] = dict()
                    monkeys[monkey]['next'] = dict()
                    monkeys[monkey]['count'] = 0
                case 2:
                    items = [int(item) for item in line.split(': ')[1].split(', ')]
                    monkeys[monkey]['items'] = items
                case 3:
                    operation_text = line.split(' = ')[1]
                    monkeys[monkey]['operation_text'] = operation_text
                case 4:
                    divisor = int(line.split(' by ')[1])

                    monkeys[monkey]['divisor'] = divisor

                case 5:
                    next = int(line.split(' monkey ')[1])
                    monkeys[monkey]['next'][True] = next
                case 6:
                    next = int(line.split(' monkey ')[1])
                    monkeys[monkey]['next'][False] = next

        multiple = 1
        for monkey in monkeys.keys():
            multiple = multiple * monkeys[monkey]['divisor']

        for i in range(10000):
            for monkey in monkeys.keys():
                for item in monkeys[monkey]['items']:
                    old = item
                    item_op = eval(monkeys[monkey]['operation_text']) % multiple

                    test_res = item_op % monkeys[monkey]['divisor']==0
                    next_monkey = monkeys[monkey]['next'][test_res]
                    monkeys[next_monkey]['items'].append(item_op)
                    monkeys[monkey]['count'] += 1

                monkeys[monkey]['items'] = []

        inspected = []
        for monkey in monkeys.keys():
            inspected.append(monkeys[monkey]['count'])
        inspected.sort()
        print(inspected)

        print(inspected[-2]*inspected[-1])