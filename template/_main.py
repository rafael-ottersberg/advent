day = 'template'
import numpy as np

for filename in [f'test.txt', 'input.txt']:
    print('_________________' + '\n' + filename)
    with open(f'{day}/{filename}') as f:
        tot_score = 0
        tot_score_part2 = 0
        for line in f.readlines():
            line = line.strip('\n')
            first, second = line.split(' ')


        print(tot_score)
        print(tot_score_part2)