day = '13'
import numpy as np

def check_order(left, right):
    if len(left)==0:
        if len(right)==0:
            return None
        else:
            #print('left empty')
            return True
    elif len(right)==0:
        #print('right empty')
        return False
        
    l, r = left[0], right[0]
    if type(l)==int and type(r)==int:
        if l==r:
            return check_order(left[1:], right[1:])
        elif l<r:
            #print(f'{l}vs{r}')
            return True
        else:
            #print(f'{l}vs{r}')
            return False
    
    if type(r) != list:
        r = [r]
    if type(l) != list:
        l = [l]
    
    corr = check_order(l, r)
    if corr is None:
        return check_order(left[1:], right[1:])
    else:
        return corr


for filename in [f'test.txt', 'input.txt']:
    lines = []
    unsorted_lines = []
    print('_________________' + '\n' + filename)
    with open(f'{day}/{filename}') as f:
        tot_score = 0
        tot_score_part2 = 0
    
        for line in f.readlines():
            line = line.strip('\n')
            lines.append(line)
            if line:
                unsorted_lines.append(eval(line))

        count = 0
        for i in range(len(lines)//3):
            left = eval(lines[3 * i])
            right = eval(lines[3 * i + 1])
            
            correct = check_order(left, right)
            if correct:
                #print(left, right)
                count+=i+1
        
        print(f'pt1: {count}')

        sorted_lines = []

        unsorted_lines.extend([[[2]],[[6]]])

        for u_line in unsorted_lines:
            line_found = False
            for i, s_line in enumerate(reversed(sorted_lines)):
                if check_order(s_line, u_line):
                    line_found = True
                    break
            if line_found:
                sorted_lines.insert(len(sorted_lines)-i, u_line)
            else:
                sorted_lines.insert(0, u_line)
        #print(sorted_lines)
        print(f'pt2: {(sorted_lines.index([[2]])+1)*(sorted_lines.index([[6]])+1)}')