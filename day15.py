import utils
import os.path
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day15_test.txt')
finput = os.path.join(dir, 'day15_input.txt')

@utils.timeit
def part1(fname):
    return _part1(utils.f2lines(fname)[0])

def _part1(s):
    res = 0

    for step in s.split(','):
        sres = 0
        for c in list(step):
            sres += ord(c)
            sres *= 17
            sres %= 256
        res += sres

    return res

def do1():
    assert 52 == _part1("HASH")
    assert 1320 == part1(ftest)
    assert 498538 == part1(finput)
