import utils
from maps import Map
import os.path
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day13_test.txt')
finput = os.path.join(dir, 'day13_input.txt')

def get_mres(lines):

    m = Map(lines)

    for mx in range(1, m.w):
        is_mirror = True
        for y in range(0, m.h):
            dx = 1
            while True:
                left = m.get(mx - dx, y)
                right = m.get(mx - 1 + dx, y)
                if left is None or right is None:
                    break
                if left != right:
                    is_mirror = False
                    break
                dx += 1
            if not is_mirror:
                break
        if is_mirror:
            return mx

    for my in range(1, m.h):
        is_mirror = True
        for x in range(0, m.w):
            dy = 1
            while True:
                top = m.get(x, my - dy)
                bottom = m.get(x, my - 1 + dy)
                if top is None or bottom is None:
                    break
                if top != bottom:
                    is_mirror = False
                    break
                dy += 1
            if not is_mirror:
                break
        if is_mirror:
            return 100 * my

    return 0 # should not happen


@utils.timeit
def part1(fname):
    res = 0

    mlines = []
    for line in utils.f2lines(fname):
        if line == '':
            res += get_mres(mlines)
            mlines.clear()
        else:
            mlines.append(line)

    return res

def do1():
    assert 405 == part1(ftest)
    assert 37381 == part1(finput)
