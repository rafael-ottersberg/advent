day = '12'
import numpy as np
import string

def waterfall(elev, visit, start, end):
    next_tiles = set([end])
    not_found = True
    number_of_rounds = 0

    while not_found:
        assert next_tiles
        reachable_tiles = set()
        for position in next_tiles:
            #if elev[position[0], position[1]]==0:  ##part 1
            if position[0] == start[0] and position[1] == start[1]:
                not_found = False
                break
            for i in range(-1,2,2):
                next_position = (position[0], position[1]+i)
                if is_reachable(elev, visit, position, next_position):
                    reachable_tiles.add(next_position)

                next_position = (position[0]+i, position[1])
                if is_reachable(elev, visit, position, next_position):
                    reachable_tiles.add(next_position)

            visit[position[0], position[1]] = 1

        if not not_found:
            break

        next_tiles = reachable_tiles
        number_of_rounds += 1
    print(number_of_rounds)


def is_reachable(elev, visit, position, next_position):
    for i in range(2):
        if next_position[i] < 0 or next_position[i] >= elev.shape[i]:
            return False
    for i in range(2):
        if elev[position[0], position[1]] - elev[next_position[0], next_position[1]] <= 1:
            if visit[next_position[0], next_position[1]] == 0:
                return True
        return False    

for filename in [f'test.txt', 'input.txt']:
    print('_________________' + '\n' + filename)
    with open(f'{day}/{filename}') as f:
        rows = []
        for i, line in enumerate(f.readlines()):
            line = line.strip('\n')
            row=[]
            for j, c in enumerate(line):
                if c == 'S':
                    c = 'a'
                    start = (i,j)
                if c == 'E':
                    c = 'z'
                    end = (i,j)
                value = string.ascii_lowercase.index(c)
                row.append(value)
            rows.append(row)

    elev = np.zeros((len(rows), len(rows[0])))
    visit = np.zeros((len(rows), len(rows[0])))
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            elev[i,j]=rows[i][j]

    print(elev)
    print(start)
    waterfall(elev, visit, start, end)
