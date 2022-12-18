day = '03'
import string

import numpy as np
for filename in [f'test.txt', 'input.txt']:
    print('_________________' + '\n' + filename)
    with open(f'{day}/{filename}') as f:
        tot_score = 0
        tot_score_pt2 = 0

        lines = []
        for line in f.readlines():
            lines.append(line)
        
        for i in range(int(len(lines)/3)):
            index = i*3

            for i1 in lines[index]:
                for i2 in lines[index+1]:
                    for i3 in lines[index+2]:
                        if i1 == i2 == i3:
                            if i1.islower():
                                tot_score += string.ascii_lowercase.index(i1) + 1
                            elif i1.isupper():
                                tot_score += string.ascii_uppercase.index(i1) + 27
                            break
                    else:
                        continue
                    break
                else:
                    continue
                break

            
        print(tot_score)
        print(tot_score_pt2)
