import utils
from maps import Map
import os.path
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day14_test.txt')
finput = os.path.join(dir, 'day14_input.txt')

@utils.timeit
def part1(fname):
    res = 0

    m = Map.from_file(fname)

    rocks = m.find_all('O')
    rocks.sort(key=lambda p: p.y)

    for r in rocks:
        m.set(r.x, r.y, '.') # remove rock
        yy = r.y
        while True:
            yy -= 1
            if m.get(r.x, yy) != '.':
                break
        m.set(r.x, yy + 1, 'O') # place rock
        load = m.h - (yy + 1)
        res += load

    return res

def do1():
    assert 136 == part1(ftest)
    assert 105623 == part1(finput)
