import utils
import os.path
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day15_test.txt')
finput = os.path.join(dir, 'day15_input.txt')

@utils.timeit
def part1(fname):
    res = 0

    return res

def do1():
    assert 1320 == part1(ftest)
    assert 498538 == part1(finput)
