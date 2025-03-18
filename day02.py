from tkinter.constants import NUMERIC

import utils
import functools
import os.path
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day02_test.txt')
finput = os.path.join(dir, 'day02_input.txt')

part1_col_max = { 'red': 12, 'green': 13, 'blue': 14 }

@utils.timeit
def part1(fname):
    res = 0

    for line in utils.f2lines(fname):
        # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        gid, game = line.split(':')
        id = int(gid.split(' ')[1])
        possible = True
        for set_of_cubes in game.split(';'): # 3 blue, 4 red
            for cubes in set_of_cubes.split(','): #  3 blue
                n_col = cubes.strip().split(' ') # number,color
                if int(n_col[0]) > part1_col_max[n_col[1]]:
                    possible = False
                    break
        if possible:
            res += id

    return res

def do1():
    assert 8 == part1(ftest)
    assert 1853 == part1(finput)

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
        res += functools.reduce(lambda x,y: x * y, mins.values())

    return res

def do2():
    assert 2286 == part2(ftest)
    assert 72706 == part2(finput)
