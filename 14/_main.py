day = '14'
import numpy as np

def move_sand(pos, cave):
    for i in [0,-1,1]:
        if cave[pos[0]+i, pos[1]+1]==0:
            return (pos[0]+i, pos[1]+1)

    return None


for filename in [f'test.txt', 'input.txt']:
    print('_________________' + '\n' + filename)
    with open(f'{day}/{filename}') as f:
        tot_score = 0
        tot_score_part2 = 0

        cave = np.zeros((1000, 1000))
        for line in f.readlines():
            line = line.strip('\n')
            nodes = line.split(' -> ')
            nodes = [np.array([int(node.split(',')[0]), int(node.split(',')[1])]) for node in nodes]
            
            for i in range(len(nodes)-1):
                diff = nodes[i]-nodes[i+1]
                for k, d in enumerate(diff):
                    if d!=0:
                        if d<0:
                            a = 1
                        else:
                            a = -1

                        for j in range(np.abs(d)+1):
                            step = np.zeros(2)
                            step[k] = a * j
                            x, y = int(nodes[i][0]+step[0]), int(nodes[i][1]+step[1])
                            cave[x,y] = 1
                    
        biggest_index = np.max(np.nonzero(np.sum(cave, axis=0)))

        in_void = False
        while not in_void:
            sand_index = (500,0)
            moving = True
            while moving:
                next_index = move_sand(sand_index, cave)
                if next_index is None:
                    moving = False
                    cave[sand_index[0], sand_index[1]] = 2
                elif next_index[1]>biggest_index:
                    in_void = True
                    break
                else:
                    sand_index = next_index
                    
        
        print(cave[494:503, :12])
        resting = cave==2
        print(np.sum(resting))


        print(tot_score)
        print(tot_score_part2)