day = '04'
import numpy as np

for filename in [f'test.txt', 'input.txt']:
    print('_________________' + '\n' + filename)
    with open(f'{day}/{filename}') as f:
        tot_score = 0
        tot_score_part2 = 0

        for line in f.readlines():
            line = line.strip('\n')
            first, second = line.split(',')
            fa, fb = first.split('-')
            sa, sb = second.split('-')
            fa, fb, sa, sb = int(fa),int(fb), int(sa), int(sb)
            #print(sa,sb)
            f = set(range(fa,fb+1))
            s = set(range(sa,sb+1))

            number = len(list(f&s))
            print(number)
            if number>0:
                tot_score+=1


        print(tot_score)
        print(tot_score_part2)