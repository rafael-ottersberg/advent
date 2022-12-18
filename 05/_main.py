day = '05'
import numpy as np

for filename in ['input.txt']:

    print('_________________' + '\n' + filename)
    with open(f'{day}/{filename}') as f:
        tot_score = 0
        tot_score_part2 = 0

        crates=dict()

        for i in range(9):
            crates[i]=[]
        line_count = 0
        for line in f.readlines():
            line = line.strip('\n')
            line_count+=1
            if line_count<9:
                for i in range(9):
                    ind = i * 4 + 1
                    if line[ind] != ' ':
                        crates[i].append(line[ind])

            elif line_count>=11:
                parts=line.split(' ')

                nr = int(parts[1])
                fr = int(parts[3]) - 1
                to = int(parts[5]) - 1
                
                move=crates[fr][0:nr]
                crates[fr] = crates[fr][nr:]
                crates[to] = move+crates[to]


        for i in range(9):
            print(crates[i][0])

        print(crates)
        print(tot_score)
        print(tot_score_part2)