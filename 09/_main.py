day = '09'
import numpy as np

def is_in_proximity(head, tail):
    dist = np.sqrt((head[0]-tail[0])**2 + (head[1]-tail[1])**2)
    return dist <= np.sqrt(2)
def is_neighbour(head, tail):
    dist = np.sqrt((head[0]-tail[0])**2 + (head[1]-tail[1])**2)
    return dist <= 1

def find_next_pos(prev, current):
    for x in range(-1,2):
        for y in range(-1,2):
            if is_neighbour(prev, (current[0]+x, current[1]+y)):
                return (current[0]+x, current[1]+y)
    for x in range(-1,2):
        for y in range(-1,2):
            if is_in_proximity(prev, (current[0]+x, current[1]+y)):
                return (current[0]+x, current[1]+y)

    raise Exception(f'not successful: {prev} {current}')
    

for filename in [f'test.txt', 'input.txt']:
    l_rope=10
    rope = [(500,500) for _ in range(l_rope)]
    occupied = np.zeros((1000,1000))
    print('_________________' + '\n' + filename)
    with open(f'{day}/{filename}') as f:
        for line in f.readlines():
            line = line.strip('\n')
            direction, moves = line.split(' ')
            for i in range(int(moves)):
                #print(rope)
                head = rope[0]
                match direction:
                    case 'R':
                        rope[0] = (head[0]+1, head[1])
                    case 'L':
                        rope[0] = (head[0]-1, head[1])
                    case 'U':
                        rope[0] = (head[0], head[1]+1)
                    case 'D':
                        rope[0] = (head[0], head[1]-1)
                
                for node in range(1, l_rope):
                    #print(node)
                    if not is_in_proximity(rope[node-1], rope[node]):
                        rope[node] = find_next_pos(rope[node-1], rope[node])
                        if node == l_rope-1:
                            occupied[rope[node][0], rope[node][1]] = 1


                


        
        print(int(np.sum(occupied)+1))
   
