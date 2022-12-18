import numpy as np
import pandas as pd
import scipy


f = open('input_01.txt')
elfs_total = []
elfs_items = []

items = []
total = 0
for line in f.readlines():
    if line == '\n':
        elfs_total.append(total)
        elfs_items.append(items)

        items = []
        total = 0
    else:
        items.append(int(line))
        total += int(line)

elfs_tot = np.array((elfs_total))

tot = 0
for i in range(3):
    index = np.argmax(elfs_tot)
    tot += elfs_tot[index]
    print(index, elfs_tot[index])
    elfs_tot = np.delete(elfs_tot, index)

print(tot)
elfs_total.sort()
print(elfs_total)

