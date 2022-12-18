day = '10'
import numpy as np



for filename in [f'test.txt', 'input.txt']:
    print('_________________' + '\n' + filename)
    pixels = np.zeros((6,40))
    with open(f'{day}/{filename}') as f:
        score = 0
        cycle = 1
        register = 1
        for line in f.readlines():
            x_pos = cycle % 40 - 1
            y_pos = (cycle - 1) // 40

            line = line.strip('\n')
            entries = line.split(' ')

            x_pos_reg = register % 40 - 1
            if (x_pos>=x_pos_reg and x_pos<x_pos_reg+3):
                pixels[y_pos, x_pos] = 1

            if (cycle+20) % 40 == 0:
                print(register * cycle)
                score += register * cycle
            
            match entries[0]:
                case 'noop':
                    cycle += 1
                case 'addx':
                    cycle += 1
                    x_pos = cycle % 40 - 1
                    y_pos = (cycle - 1) // 40
                    x_pos_reg = register % 40 - 1
                    if (x_pos>=x_pos_reg and x_pos<x_pos_reg+3):
                        pixels[y_pos, x_pos] = 1

                    if (cycle+20) % 40 == 0:
                        print(register * cycle)
                        score += register * cycle
                    cycle += 1
                    register += int(entries[1])



        print(score)
        lines = []
        for i in range(pixels.shape[0]):
            line = str()
            for j in range(pixels.shape[1]):
                if pixels[i,j] == 1:
                    c = '#'
                else:
                    c='.'
                line += c

            print(line)