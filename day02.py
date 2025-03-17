import utils
from collections import Counter
import os.path
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day02_test.txt')
finput = os.path.join(dir, 'day02_input.txt')

part1_col_max = { 'red': 12, 'green': 13, 'blue': 14 }

#Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

@utils.timeit
def part1(fname):
    res = 0

    for line in utils.f2lines(fname):
        gid, game = line.split(':')
        id = int(gid.split(' ')[1])
        possible = True
        for set_of_cubes in game.split(';'):
            for cubes in set_of_cubes.split(','):
                n_col = cubes.strip().split(' ')
                if int(n_col[0]) > part1_col_max[n_col[1]]:
                    possible = False
        if possible:
            res += id

    return res

def do1():
    assert 8 == part1(ftest)
    assert 1853 == part1(finput)

do1()

@utils.timeit
def part2(fname):
    res = 0

    for line in utils.f2lines(fname):
        mins = { 'red': 0, 'green': 0, 'blue': 0 }
        for set_of_cubes in line.split(':')[1].split(';'):
            for cubes in set_of_cubes.split(','):
                n_col = cubes.strip().split(' ')
                n = int(n_col[0])
                col = n_col[1]
                mins[col] = max(mins[col], n)
        res += mins['red'] * mins['green'] * mins['blue']

    return res

def do2():
    assert 2286 == part2(ftest)
    assert 72706 == part2(finput)
