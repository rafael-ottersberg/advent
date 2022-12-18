day = '18'
import numpy as np
import sys
import time
sys.setrecursionlimit(30000)

for filename in [f'test.txt', 'input.txt']:
    print('_________________' + '\n' + filename)
    with open(f'{day}/{filename}') as f:
        tot_score = 0
        tot_score_part2 = 0

        t1 = time.time()
        size = 22
        grid = np.zeros((size,size,size))
        c = set()
        for line in f.readlines():
            line = line.strip('\n')
            x,y,z = [int(i) for i in line.split(',')]

            count = 0
            for i in [-1, 1]:
                if (x+i,y,z) in c:
                    count += 1
                if (x,y+i,z) in c:
                    count += 1
                if (x,y,z+i) in c:
                    count += 1

            c.add((x,y,z))

            tot_score += 6 - (2*count)

            grid[x,y,z] = 1
        
        t2 = time.time()
        print(f'task 1: {t2-t1:.4f}s')

        def flood(cave, coord):
            x,y,z = coord
            for i in [-1, 1]:
                if (x+i) < size and (x+i) >= 0:
                    if cave[x+i,y,z] == 0:
                        cave[x+i,y,z] = 2
                        cave = flood(cave, (x+i,y,z))
                if (y+i) < size and (y+i) >= 0:
                    if cave[x,y+i,z] == 0:
                        cave[x,y+i,z] = 2
                        cave = flood(cave, (x,y+i,z))
                if (z+i) < size and (z+i) >= 0:
                    if cave[x,y,z+i] == 0:
                        cave[x,y,z+i] = 2
                        cave = flood(cave, (x,y,z+i))
            return cave

        t1 = time.time()
        grid = flood(grid, (0,0,0))

        holes = []
        for x in range(size):
            for y in range(size):
                for z in range(size):
                    if grid[x,y,z]==0:
                        holes.append((x,y,z))
        c_holes = set()
        for h in holes:
            x,y,z = h
            count = 0
            for i in [-1,1]:
                if (x+i,y,z) in c_holes:
                    count += 1
                if (x,y+i,z) in c_holes:
                    count += 1
                if (x,y,z+i) in c_holes:
                    count += 1

            c_holes.add((x,y,z))

            tot_score_part2 += 6 - (2*count)
        t2 = time.time()
        print(f'task 2: {t2-t1:.4f}s')
               

        print(tot_score)
        print(tot_score-tot_score_part2)