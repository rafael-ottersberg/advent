day = '19'
import numpy as np
import re
import time

for filename in [f'test.txt']:#, 'input.txt']:
    print('_________________' + '\n' + filename)
    with open(f'{day}/{filename}') as f:
        tot_score = 0
        tot_score_part2 = 0
        blueprints = dict()
        for line in f.readlines():
            line = line.strip('\n')
            i, ore_ore, clay_ore, obs_ore, obs_clay, geo_ore, geo_obs = [int(nr) for nr in re.findall('[0-9]+', line)]
            
            blueprints[i] = dict()
            blueprints[i]['ore'] = {'ore': ore_ore}
            blueprints[i]['clay'] = {'ore': clay_ore}
            blueprints[i]['obs'] = {'ore': obs_ore, 'clay': obs_clay}
            blueprints[i]['geo'] = {'ore': geo_ore, 'obs': geo_obs}

        results = dict()

        def decide(args):
            minutes_left, money, robots, blueprint_index = args 
            blueprint = blueprints[blueprint_index]
            buy_robo = dict()
            for robo_kind in ['ore', 'clay', 'obs', 'geo']:
                buy_robo[robo_kind] = True

            for kind in ['ore', 'clay', 'obs']:
                for robo_kind in ['ore', 'clay', 'obs', 'geo']:
                    if kind in blueprint[robo_kind].keys():
                        if blueprint[robo_kind][kind] > money[kind]:
                            buy_robo[robo_kind] = False

            for kind in robots.keys():
                money[kind] += robots[kind]
            
            minutes_left -= 1
            max_geo = 0
            if minutes_left > 0:
                if buy_robo['geo']:
                    robo = 'geo'
                    money_robo = money.copy()
                    robots_robo = robots.copy()
                    for kind in blueprint[robo].keys():
                        money_robo[kind] -= blueprint[robo][kind]
                        robots_robo[robo] += 1
                        args = (minutes_left, money_robo, robots_robo, blueprint_index)
                        if args in results.keys():
                            geo = results[args]
                        else:
                            geo = decide(args)
                        max_geo = max(geo, max_geo)
                
                else:
                    args = (minutes_left, money, robots, blueprint_index)
                    if args in results.keys():
                        geo = results[args]
                    else:
                        geo = decide(args)
                    max_geo = max(geo, max_geo)

                    for robo in buy_robo.keys():
                        if buy_robo[robo]:
                            money_robo = money.copy()
                            robots_robo = robots.copy()
                            for kind in blueprint[robo].keys():
                                money_robo[kind] -= blueprint[robo][kind]
                                robots_robo[robo] += 1
                                args = (minutes_left, money_robo, robots_robo, blueprint_index)
                                if args in results.keys():
                                    geo = results[args]
                                else:
                                    geo = decide(args)
                                max_geo = max(geo, max_geo)

            return max_geo


        money = {
            'ore': 0,
            'clay': 0,
            'obs': 0,
            'geo': 0
            }

        robots = {
            'ore': 1,
            'clay': 0,
            'obs': 0,
            'geo': 0
            }


        t1 = time.time()
        args = (24, money, robots, 1)
        tot_score = decide(args)
        t2 = time.time()

        print(f'{t2-t1:.2f}s')
        print(tot_score)