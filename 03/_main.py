day = '03'
import string

import numpy as np
for filename in [f'test.txt', 'input.txt']:
    print('_________________' + '\n' + filename)
    with open(f'{day}/{filename}') as f:
        tot_score = 0
        tot_score_pt2 = 0
        for line in f.readlines():
            line = line.strip('\n')
            noi = int(len(line)/2)
            pt1 = line[:noi]
            pt2 = line[noi:]

            for item in pt1:
                for item2 in pt2:
                    if item == item2:
                        #print(item, item2)
                        if item.islower():
                            tot_score += string.ascii_lowercase.index(item) + 1
                        elif item.isupper():
                            tot_score += string.ascii_uppercase.index(item) + 27
                        break
                else:
                    continue
                break
            

        print(tot_score)
        print(tot_score_pt2)
