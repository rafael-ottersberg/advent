day = '16'
import numpy as np
import re
from queue import PriorityQueue
import time

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight=1):
        self.edges[u][v] = weight
    
def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D

for filename in [f'test.txt', 'input.txt']:
    print('_________________' + '\n' + filename)
    with open(f'{day}/{filename}') as f:
        tot_score = 0
        tot_score_part2 = 0

        vertices_dict = dict()
        number_dict = dict()
        vertices_list = []
        flowing_vertices = []

        for i, line in enumerate(f.readlines()):
            line = line.strip('\n')
            pattern_vertices = r'[A-Z]{2}'
            pattern_flow = r'[0-9]+'
            flow = int(re.findall(pattern_flow, line)[0])
            vertices = re.findall(pattern_vertices, line)
            vertex = vertices[0]
            neighbours = vertices[1:]
            vertices_dict[vertex] = dict()
            vertices_dict[vertex]['neighbours'] = neighbours
            vertices_dict[vertex]['flow'] = flow

            number_dict[vertex] = i
            vertices_list.append(vertex)
            if flow != 0:   
                flowing_vertices.append(i)
        
        edges = set()
        flow_dict = dict()
        for vertex in vertices_dict.keys():
            flow_dict[number_dict[vertex]] = vertices_dict[vertex]['flow']
            for neighbour in vertices_dict[vertex]['neighbours']:
                edges.add((number_dict[vertex], number_dict[neighbour]))

        #print(edges)

    g = Graph(len(vertices_dict))
    for edge in edges:
        g.add_edge(edge[0], edge[1])


    distances = dict()
    for i in range(len(vertices_list)):
        g = Graph(len(vertices_dict))
        for edge in edges:
            g.add_edge(edge[0], edge[1])
        distances[i] = dijkstra(g,i)

    # print(vertices_list)
    # print(flow_dict)
    minutes_left = 30
    current_pos = 0
    tot_score = 0
    unopened_valves = set(flowing_vertices)

    def check_next_steps(minutes_left, current_pos, unopened_valves):
        if minutes_left <= 0:
            return 0, []

        distance_dict = distances[current_pos]
        
        max_score_left = 0
        valves = []

        for v in unopened_valves:
            minutes_left_next = minutes_left - distance_dict[v] - 1
            if minutes_left_next <= 0:
                continue
            curr_score = minutes_left_next * flow_dict[v]
            next_unopened_valves = unopened_valves.copy()
            next_unopened_valves.remove(v)
            score_left, returned_valves = check_next_steps(minutes_left_next, v, next_unopened_valves)
            #print(v, score_left, valves)
            score_left += curr_score

            if score_left > max_score_left:
                max_score_left = score_left
                returned_valves.append(v)
                valves = returned_valves

        #print(next_v)
        return max_score_left, valves

    def check_next_steps_both(busy_until1, busy_until2, pos1, pos2, unopened_valves):
        global results
        global calc
        global stored
        minutes_left = max(busy_until1, busy_until2)
        if minutes_left <= 0:
            return 0
                
        max_score_left = 0
        check1 = busy_until1 >= busy_until2
        
        if check1:
            pos = pos1
        else:
            pos = pos2

        for v in unopened_valves:
            distance_dict = distances[pos]

            minutes_left_next = minutes_left - distance_dict[v] - 1
            if minutes_left_next <= 0:
                continue

            score = minutes_left_next * flow_dict[v]

            next_unopened_valves = unopened_valves.copy()
            next_unopened_valves.remove(v)
            if check1:
                args = (minutes_left_next, busy_until2, v, pos2, next_unopened_valves)
            else:
                args = (busy_until1, minutes_left_next, pos1, v, next_unopened_valves)
            
            if args[0] < args[1]:    
                hashable_args = (args[0], args[1], args[2], args[3], tuple(args[4]))
            else:
                hashable_args = (args[1], args[0], args[3], args[2], tuple(args[4]))

            if hashable_args in results.keys():
                score_left = results[hashable_args]
                stored += 1
            else:
                score_left = check_next_steps_both(*args)
                results[hashable_args] = score_left
                calc += 1
                
            #print(v, score_left, valves)
            score_left += score

            if score_left > max_score_left:
                max_score_left = score_left

        #print(next_v)
        return max_score_left

    t1 = time.time()
    starting_field = number_dict['AA']
    tot_score, valves = check_next_steps(30, starting_field, unopened_valves)
    t2 = time.time()
    print(t2 - t1)
    print(tot_score)
    print(valves)

    
    unopened_valves = set(flowing_vertices)
    minutes_left = 26
    pos_1 = starting_field
    pos_2 = starting_field
    next_you = 0
    next_ele = 0

    t1 = time.time()
    results = dict()
    calc = 0
    stored = 0
    tot_score = check_next_steps_both(minutes_left, minutes_left, pos_1, pos_2, unopened_valves)
    t2 = time.time()
    print(t2 - t1)  
    print(tot_score)
    print(f'{calc=} {stored=}')
