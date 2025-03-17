import utils
import os.path
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day19_test.txt')
finput = os.path.join(dir, 'day19_input.txt')

@utils.timeit
def part1(fname):
    res = 0

    return res

def do1():
    assert 19114 == part1(ftest)
    assert 476889 == part1(finput)
