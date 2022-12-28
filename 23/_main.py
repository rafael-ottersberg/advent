day = '23'
import numpy as np
import time


directions = {
    (1,0): [(1,1), (1,0), (1,-1)], 
    (0,1): [(1,1), (0,1), (-1,1)], 
    (-1,0): [(-1,1),(-1,0),(-1,-1)],
    (0,-1): [(1,-1),(0,-1),(-1,-1)]}

neighbors = [(1,1), (1,0), (1,-1), (0,1), (0,-1), (-1,1), (-1,0), (-1,-1)]

for filename in [f'test.txt', 'input.txt']:
    print('_________________' + '\n' + filename)
    with open(f'{day}/{filename}') as f:
        elves = set()
        for i, line in enumerate(f.readlines()):
            line = line.strip('\n')
            for j, field in enumerate(line):
                if field == '#':
                    elves.add((i,j))

        dirs = [(-1,0), (1,0), (0,-1), (0,1)]

        t1 = time.time()
        i = 0
        while True:
            i += 1

            next_elves = dict()
            duplicate_elves = set()
            for elve in elves:
                stay = True
                for neigh in neighbors:
                    coord = (elve[0]+neigh[0], elve[1]+neigh[1])
                    if coord in elves:
                        stay = False
                        break
                
                if not stay:
                    for dir in dirs:
                        move_here = True
                        for neigh in directions[dir]:
                            coord = (elve[0]+neigh[0], elve[1]+neigh[1])
                            if coord in elves:
                                move_here = False
                                break
                    
                        if move_here:
                            coord = (elve[0]+dir[0], elve[1]+dir[1])
                            if not coord in next_elves.keys():
                                next_elves[coord] = [elve]

                            else:
                                next_elves[coord].append(elve)
                                duplicate_elves.add(coord)
                            break
                        else:
                            continue
                    else:
                        next_elves[elve] = [elve]

                else:
                    next_elves[elve] = [elve]

            finish_program = True
            for elve in next_elves.keys():
                if next_elves[elve] != [elve]:
                    finish_program = False
                    break
            
            if finish_program:
                print(f'pt2: {i}')
                break

            elves = set(next_elves.keys())
            for dup in duplicate_elves:
                elves.remove(dup)
                for elve in next_elves[dup]:
                    elves.add(elve)

            dirs = dirs[1:] + dirs[:1]

            if i == 10:
                min_x = min([e[0] for e in elves])
                max_x = max([e[0] for e in elves])
                min_y = min([e[1] for e in elves])
                max_y = max([e[1] for e in elves])

                size = (max_x-min_x+1)*(max_y-min_y+1)
                print(f'pt1: {size-len(elves)}')
                t2 = time.time()
                print(f'time pt1: {t2-t1:.4f}')

        
        t2 = time.time()
        print(f'time pt2: {t2-t1:.4f}')


