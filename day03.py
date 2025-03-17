import utils
from maps import Map, Pos
import os.path
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day03_test.txt')
finput = os.path.join(dir, 'day03_input.txt')

# read digits left of position
def read_left(m, p):
    res, n = '', 0
    while True:
        n += 1
        s = m.get(p.x - n, p.y)
        if s is None or s == '.':
            break
        res = s + res
    return res

# read digits right of position
def read_right(m, p):
    res, n = '', 0
    while True:
        n += 1
        s = m.get(p.x + n, p.y)
        if s is None or s == '.':
            break
        res += s
    return res

def add_if_n(res, n):
    if n != '':
        res.append(int(n))

# read top and bottom
def read_tb(m, pp, res):
    t = m.get(pp.x, pp.y)
    if t is not None: # so we're reading inside the map
        tl = read_left(m, pp)
        tr = read_right(m, pp)
        for n in (tl + t + tr).split('.'):
            add_if_n(res, n)

def get_numbers_around(m, p):
    res = []
    add_if_n(res, read_left(m, p))
    add_if_n(res, read_right(m, p))
    read_tb(m, Pos(p.x, p.y - 1), res)
    read_tb(m, Pos(p.x, p.y + 1), res)
    return res

@utils.timeit
def part1(fname):
    res = 0

    skip = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

    m = Map(fname)
    for s in m.get_symbols():
        if s not in skip:
            for p in m.find_all(s):
                for n in get_numbers_around(m, p):
                    res += n

    return res

def do1():
    assert 4361 == part1(ftest)
    assert 520135 == part1(finput)

@utils.timeit
def part2(fname):
    res = 0

    m = Map(fname)
    for p in m.find_all('*'):
        ns = get_numbers_around(m, p)
        if len(ns) == 2:
            res += ns[0] * ns[1]

    return res

def do2():
    assert 467835 == part2(ftest)
    assert 72514855 == part2(finput)
