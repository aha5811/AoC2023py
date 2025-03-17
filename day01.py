import utils
from collections import Counter
import os.path
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day01_test.txt')
ftest2 = os.path.join(dir, 'day01_test2.txt')
finput = os.path.join(dir, 'day01_input.txt')

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

@utils.timeit
def part1(fname):
    res = 0

    for line in utils.f2lines(fname):
        first, _, last, _ = find(line, digits)
        res += first * 10 + last

    return res

def find(line, digits):
    first, min, last, max = None, None, None, None
    for idx in range(len(digits)):
        d = digits[idx]
        v = idx + 1
        if d in line:
            i = line.find(d)
            if min is None or i < min:
                first = v
                min = i
            i = line.rfind(d)
            if max is None or i > max:
                last = v
                max = i
    return first, min, last, max

def do1():
    assert 142 == part1(ftest)
    assert 54708 == part1(finput)

digitsW = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

@utils.timeit
def part2(fname):
    res = 0

    for line in utils.f2lines(fname):
        first, min, last, max = find(line, digits)
        firstW, minW, lastW, maxW = find(line, digitsW)
        ff = first if min is not None and (minW is None or min < minW) else firstW
        ll = last if max is not None and (maxW is None or max > maxW) else lastW
        res += ff * 10 + ll

    return res

def do2():
    assert 281 == part2(ftest2)
    assert 54087 == part2(finput)
