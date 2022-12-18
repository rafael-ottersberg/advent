day = '06'
import numpy as np

for filename in [f'test.txt', 'input.txt']:
    print('_________________' + '\n' + filename)
    with open(f'{day}/{filename}') as f:
        tot_score = 0
        tot_score_part2 = 0
        for line in f.readlines():
            line = line.strip('\n')

            for i in range(len(line)-14):
                if len(set(line[i:i+14])) == 14:
                    print(i+14, line[i:i+14])
                    break


        print(tot_score)
        print(tot_score_part2)