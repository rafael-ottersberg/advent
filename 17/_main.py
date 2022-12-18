day = '17'
import numpy as np

class Stone():
    def __init__(self, i):
        self.edge = set()

        self.add_edges(i)
    
    def add_edges(self, i):
        match i:
            case 0:
                for x in range(4):
                    self.edge.add((x,0))
            case 1:
                for x in range(3):
                    if x == 0 or x == 2:
                        self.edge.add((x,1))
                    else:
                        self.edge.add((x,0))
                        self.edge.add((x,1))
                        self.edge.add((x,2))
            case 2:
                for x in range(3):
                    self.edge.add((x,0))
                for y in range(2):
                    self.edge.add((2,1+y))
            case 3:
                for y in range(4):
                    self.edge.add((0, y))
            case 4:
                for x in range(2):
                    for y in range(2):
                        self.edge.add((x,y))

stones = dict()
for i in range(5):
    stones[i] = Stone(i)

def draw_rock(pos, rock, cave):
    for e in rock.edge:
        x = e[0] + pos[0]
        y = e[1] + pos[1]
        cave[x, y] = 1

    return cave

for filename in ['test.txt', 'input.txt']:
    print('_________________' + '\n' + filename)
    with open(f'{day}/{filename}') as f:
        tot_score = 0
        tot_score_part2 = 0
        go_left = []
        for line in f.readlines():
            line = line.strip('\n')
            for dir in line:
                if dir == '<':
                    go_left.append(True)
                else:
                    go_left.append(False)
        
        

        def simulate(number_of_rocks, last_state=None):
            states = set()
            states_list = []
            height_list = []

            if last_state is None:
                additional_height = 0
            else:
                additional_height = -min(last_state[0]) + 1

            print(f'{additional_height=}')

            cave = np.zeros((7,2*number_of_rocks+additional_height+10))
            cave[:,0] = 1

            if last_state is not None:
                for i in range(len(last_state[0])):
                    cave[i, last_state[0][i] + additional_height] = 1
            
            print(np.sum(cave))
        
            jet_counter = 0
            jet_length = len(go_left)

            if last_state is not None:
                jet_counter = last_state[2] 
            
            start = 0
            if last_state is not None:
                start = last_state[1]
                
            for i in range(number_of_rocks):
                biggest_index = np.max(np.nonzero(np.sum(cave, axis=0)))

                rp = (2, biggest_index+4)
                
                rock = stones[(i + start) % 5]
                moving = True
                while moving:
                    ### left right
                    gl = go_left[jet_counter % jet_length]
                    if gl:
                        rp = (rp[0]-1, rp[1])
                    else:
                        rp = (rp[0]+1, rp[1])
                    
                    for e in rock.edge:
                        pos = (rp[0] + e[0], rp[1] + e[1])
                        #print(pos)
                        if (pos[0] < 0) or (pos[0] >= 7) or (cave[pos[0], pos[1]] == 1):
                            if not gl:
                                rp = (rp[0]-1, rp[1])
                                break
                            else:
                                rp = (rp[0]+1, rp[1])
                                break

                    jet_counter += 1
                    #print(rp)

                    ### move down
                    rp = (rp[0], rp[1] - 1)
                    for e in rock.edge:   
                        pos = (rp[0] + e[0], rp[1] + e[1])          
                        if (cave[pos[0], pos[1]] == 1):
                            rp = (rp[0], rp[1]+1)
                            moving = False
                            #print('stop moving')
                            break

                cave = draw_rock(rp, rock, cave)
                height = np.max(np.nonzero(np.sum(cave, axis=0)))
                last_rock = [np.max(np.nonzero(cave[j,:]))-height for j in range(cave.shape[0])]
                #print(last_rock)
                last_rock = tuple(last_rock)

                height = height - additional_height
                
                state = (last_rock, (i + start + 1) % 5, jet_counter % jet_length)
            
                if state in states:
                    curr_index = i
                    last_index = states_list.index(state)
                    last_height = height_list[last_index]
                    height_difference = height - last_height
                    index_difference = i - last_index
                    print(f'{last_index=} {last_height=} {curr_index=} {height_difference=}')
                    return last_height, last_index, height_difference, index_difference, state
                else:
                    states.add(state)
                    states_list.append(state)
                    height_list.append(height)
                
            

            return height, None, None, None, state

        number_test_of_rocks = 4000
        number_of_rocks = 1000000000000
        last_height, last_index, height_difference, index_difference, last_state = simulate(number_test_of_rocks)
        
        
        print(last_state)
        print(last_height)

        factor = (number_of_rocks - last_index - 1) // index_difference
        rest = (number_of_rocks - last_index - 1) % index_difference

        print(f'{factor=} {rest=}')

        rest_height, _, _, _, _ = simulate(rest, last_state)

        print(f'{rest_height=}')
        print(last_height + factor*height_difference + rest_height)


