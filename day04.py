import utils
import re
import os.path
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day04_test.txt')
finput = os.path.join(dir, 'day04_input.txt')

#Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53

@utils.timeit
def part1(fname):
    res = 0

    def to_n(s):
        return utils.s2is(re.sub("\\s+", ' ', s).strip(), ' ')

    for line in utils.f2lines(fname):
        right = line.split(':')[1].split('|')
        winning = to_n(right[0])
        mine = to_n(right[1])
        cnt = 0
        for n in mine:
            if n in winning:
                cnt += 1
        if cnt > 0:
            res += 2 ** (cnt - 1)

    return res

def do1():
    assert 13 == part1(ftest)
    assert 24542 == part1(finput)
