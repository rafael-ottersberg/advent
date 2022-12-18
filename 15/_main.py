day = '15'
import numpy as np
import re
import pickle

for filename in ['input.txt']:
    print('_________________' + '\n' + filename)
    with open(f'{day}/{filename}') as f:
        tot_score = 0
        tot_score_part2 = 0

        min_x, max_x = 0, 0
        min_y, max_y = 0, 0
        sensors = []
        beacons = set()
        for line in f.readlines():
            line = line.strip('\n')
            x1, y1, x2, y2 = [int(nr) for nr in re.findall('-?[0-9]+', line)]

            sensor = np.array([x1,y1])
            beacon = np.array([x2,y2])
            distance = np.sum(np.abs(beacon-sensor))

            beacons.add((x2,y2))

            sensors.append((sensor, distance))

        def p2_1(sensors):

            edges = set()
            edges2 = set()
            edges3 = set()
            edges4 = set()

            start = 0
            size = 4000000
            for st, sensor in enumerate(sensors):
                if st<start:
                    continue
                print(st)
                print(f'sensor: {sensor}')
                pos = sensor[0]
                dist = sensor[1]
                for i in range(dist+2):
                    for a in [-1,1]:
                        x = pos[0] + a*i
                        if x>=0 and x<=size:
                            for b in [-1,1]:
                                y = pos[1] + ((dist+1)-i)*b
                                if y>=0 and y<=size:
                                    edge = (x,y)
                                    if edge not in edges:
                                        edges.add(edge)
                                    elif edge not in edges2:
                                        edges2.add(edge)
                                    elif edge not in edges3:
                                        edges3.add(edge)
                                    elif edge not in edges4:
                                        edges4.add(edge)
            print(len(edges3))
            print(len(edges4))
            print(edges4)

            return edges4

        def p2_2(sensors, edges):
            for e in edges:
                edge = np.array([e[0],e[1]])

                no_other = True
                for sensor2 in sensors:
                    dist = np.sum(np.abs(sensor2[0]-edge))
                    if dist <= sensor2[1]:
                        no_other = False
                        break

                if no_other:
                    print(f'solution {edge}')
                    print(edge[0]*4000000+edge[1])



        def p1(sensors):
            y = 2000000
            checked = set()
            for sensor in sensors:
                pos = np.array([sensor[0][0], y])
                dist = np.sum(np.abs(sensor[0]-pos))
                if dist <= sensor[1]:
                    diff = sensor[1] - dist
                    for i in range(diff+1):
                        for a in [-1,1]:
                            p = (pos[0]+a*i, pos[1])
                            if p not in beacons:
                                checked.add(p)

            print(len(checked))
        
        import time

        t1 = time.time()
        p1(sensors)
        t2 = time.time()
        print(f'{t2-t1:.2f}s')

        t1 = time.time()
        edges = p2_1(sensors)
        t2 = time.time()
        print(f'{t2-t1:.2f}s')

        t1 = time.time()
        p2_2(sensors, edges)
        t2 = time.time()
        print(f'{t2-t1:.2f}s')

