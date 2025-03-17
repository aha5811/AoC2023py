import utils
import os.path
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day14_test.txt')
finput = os.path.join(dir, 'day14_input.txt')

@utils.timeit
def part1(fname):
    res = 0

    return res

def do1():
    assert 136 == part1(ftest)
    assert 105623 == part1(finput)
