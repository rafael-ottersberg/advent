day = '08'
import numpy as np

for filename in [f'test.txt', 'input.txt']:
    print('_________________' + '\n' + filename)
    with open(f'{day}/{filename}') as f:
        tot_score = 0
        tot_score_part2 = 0
        rows = []
        for line in f.readlines():
            line = line.strip('\n')
            cols =  []
            for char in line:
                cols.append(int(char))
            rows.append(cols)
        
        trees = np.array(rows)
        visible = np.zeros(trees.shape)
        
        rws, clms = trees.shape

        for r in range(rws):
            direction_maxes = [-1, -1]
            for c in range(clms):
                if trees[r,c] > direction_maxes[0]:
                    if visible[r,c]==0:
                        tot_score += 1
                        visible[r,c] = 1

                    direction_maxes[0] = trees[r,c]
            
            for i in range(rws):
                c = clms-i-1
                if trees[r,c] > direction_maxes[1]:
                    if visible[r,c]==0:
                        tot_score += 1
                        visible[r,c] = 1

                    direction_maxes[1] = trees[r,c]
        
        for c in range(clms):
            direction_maxes = [-1, -1]
            for r in range(rws):
                if trees[r,c] > direction_maxes[0]:
                    if visible[r,c]==0:
                        tot_score += 1
                        visible[r,c] = 1

                    direction_maxes[0] = trees[r,c]
            
            for i in range(rws):
                r = rws-i-1
                if trees[r,c] > direction_maxes[1]:
                    if visible[r,c]==0:
                        tot_score += 1
                        visible[r,c] = 1
                        
                    direction_maxes[1] = trees[r,c]

    







        print(tot_score)
        print(tot_score_part2)