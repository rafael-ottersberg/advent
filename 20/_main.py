day = '20'
import numpy as np
import time

key = 811589153

for filename in ['test.txt', 'input.txt']:
    print('_________________' + '\n' + filename)
    with open(f'{day}/{filename}') as f:
        tot_score = 0
        tot_score_part2 = 0
        numbers = []
        for line in f.readlines():
            line = line.strip('\n')
            number = int(line)*key
            numbers.append(number)
        
        ind = list(range(len(numbers)))
        nr_elements = len(numbers)

        t1 = time.time()
        for _ in range(10):
            for i in range(len(numbers)):
                index = ind[i]
                #element = numbers[index]
                element = numbers[i]
                move = element % (nr_elements - 1)
                #del numbers[index]
                new_index = (index + move - 1) % (nr_elements - 1) + 1

                #numbers.insert(new_index, element)
                for j in range(len(ind)):
                    if ind[j] > index:
                        ind[j] -= 1
                    if ind[j] >= new_index:
                        ind[j] += 1
                
                ind[i] = new_index
                #assert len(set(ind)) == len(ind)
        t2 = time.time()

        print(f'{t2-t1:.4f}s')

        #ind_zero = numbers.index(0)
        ind_zero = ind[numbers.index(0)]
        print(ind_zero)

        for i in range(1,4):
            #summand = numbers[(ind_zero + 1000*i) % nr_elements]
            summand = numbers[ind.index((ind_zero + 1000*i) % nr_elements)]
            print(summand)
            tot_score += summand

        print(tot_score)
        print(tot_score_part2)