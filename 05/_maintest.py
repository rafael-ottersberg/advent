day = '05'
import numpy as np

for filename in ['test.txt']:

    print('_________________' + '\n' + filename)
    with open(f'{day}/{filename}') as f:
        tot_score = 0
        tot_score_part2 = 0

        

        crates=dict()

        for i in range(3):
            crates[i]=[]
        line_count = 0
        for line in f.readlines():
            line = line.strip('\n')
            line_count+=1
            if line_count<4:
                for i in range(3):
                    ind = i * 4 + 1
                    #print(line[ind])
                    if line[ind] != ' ':
                        crates[i].append(line[ind])

            elif line_count>=6:
                parts=line.split(' ')

                nr = int(parts[1])
                fr = int(parts[3]) - 1
                to = int(parts[5]) - 1
                print(crates[fr], crates[to])
                for i in range(nr):
                    move=crates[fr][0:1]
                    crates[fr] = crates[fr][1:]
                    crates[to] = move+crates[to]
                print(crates[fr], crates[to])


        for i in range(3):
            print(crates[i][0])

        print(crates)
        print(tot_score)
        print(tot_score_part2)