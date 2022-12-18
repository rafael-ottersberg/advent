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
        top, bot, left, right = np.ones(trees.shape), np.ones(trees.shape), np.ones(trees.shape), np.ones(trees.shape)
        
        rws, clms = trees.shape

        for r in range(rws):
            for c in range(clms):
                if r > 0:
                    for rl in range(r):
                        if r!=r-rl:
                            if trees[r,c] > trees[r-rl,c]:
                                left[r,c] = left[r,c]+1
                            else:
                                break
                for rr in range(rws-r-1):
                    if r!=r+rr:
                        if trees[r,c] > trees[r+rr,c]:
                            right[r,c] += 1
                        else:
                            break

                if c > 0:
                    for ct in range(c):
                        if c!=c-ct:
                            if trees[r,c] > trees[r,c-ct]:
                                top[r,c] += 1
                            else:
                                break

                for cb in range(clms-c-1):
                    if c!=c+cb:
                        if trees[r,c] > trees[r,c+cb]:
                            bot[r,c] += 1
                        else:
                            break
        
        view = right*left*top*bot

        print(right)
        print(left)
        print(top)
        print(bot)
        print(np.max(view[1:rws-1, 1:clms-1]))