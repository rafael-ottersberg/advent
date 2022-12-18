import numpy as np

op_dict = {'A': 1, 'B': 2, 'C': 3}
you_dict = {'X': 1, 'Y': 2, 'Z': 3}
diff_dict = {'X': 2, 'Y': 0, 'Z': 1}
score_dict = {0: 3, 1: 6, 2: 0}

f = open('02/input_02.txt')

tot_score = 0
tot_score_part2 = 0
for line in f.readlines():
    line = line.strip('\n')
    op, you = line.split(' ')

    op_int = op_dict[op]
    you_int = you_dict[you]
    diff_int = diff_dict[you]

    diff = (you_int - op_int) % 3
    score = score_dict[diff]    
    tot_score += you_int + score

    # part2
    """
    for i in range(3):
        you_int = i + 1
        diff = (you_int - op_int) % 3
        if diff_int == diff:
            tot_score_part2 += you_int + score_dict[diff_int]
            break
    """
    you_int = (((diff_int + op_int) - 1) % 3) + 1 
    tot_score_part2 += you_int + score_dict[diff_int]

print(tot_score)
print(tot_score_part2)

f.close()