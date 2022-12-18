day = '07'
import numpy as np

for filename in [f'test.txt', 'input.txt']:
    print('_________________' + '\n' + filename)
    filesystem = {'/': dict()}

    current_folder_path = []
    with open(f'{day}/{filename}') as f:
        tot_score = 0
        tot_score_part2 = 0
        for line in f.readlines():
            line = line.strip('\n')
            shell = line.split(' ')
            if shell[0] == '$':
                if shell[1] == 'cd':
                    nextdir = shell[2]
                    if nextdir == '..':
                        current_folder_path.pop()
                    else:
                        current_folder_path.append(nextdir)
                else:
                    cmd = shell[1]

            elif shell[0] == 'dir':
                dirname = shell[1]
                lfs = filesystem
                for folder in current_folder_path:
                    lfs = lfs[folder]
                lfs[dirname] = dict()

            elif shell[0] != 'dir':
                size, filename = int(shell[0]), shell[1]
                lfs = filesystem
                for folder in current_folder_path:
                    lfs = lfs[folder]
                lfs[filename] = size

    foldersizes = []
                
    def folder_size(folder, foldersizes):
        size = 0
        
        for key in folder.keys():
            if isinstance(folder[key], dict):
                fsz, foldersizes = folder_size(folder[key], foldersizes)
                #assert not key in foldersizes.keys()
                foldersizes.append(fsz)
                size += fsz

            else:
                size += folder[key]
                assert isinstance(folder[key], int)

        return size, foldersizes

    size, _ = folder_size(filesystem, foldersizes)

    total = 0
    for sz in foldersizes:
        if sz <= 100000:
            #print(key, foldersizes[key])
            total += sz
    print(total)


    print(size)
    required = size - 70000000 + 30000000
    print(f"req: {required}")

    foldersizes.sort()
    for fs in foldersizes:
        if fs >= required:
            print("foldersize: " + str(fs))
            break