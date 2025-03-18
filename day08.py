import utils
import os.path
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day08_test.txt')
ftest2 = os.path.join(dir, 'day08_test2.txt')
finput = os.path.join(dir, 'day08_input.txt')

class Node:
    def __init__(self, l, r):
        self.r = r
        self.l = l

@utils.timeit
def part1(fname):

    instr = None
    nm = {} # node name -> node

    for line in utils.f2lines(fname):
        if instr is None:
            instr = line
        elif "=" in line:
            # AAA = (BBB, CCC)
            n_rl = line.split("=")
            n = n_rl[0].strip()
            l, r = n_rl[1].strip()[1:-1].split(',')
            nm[n] = Node(l, r.strip())

    ii = 0 # instruction index
    nn = 'AAA' # node name
    step = 0

    while True:
        step += 1
        i = instr[ii]
        n = nm[nn]
        nn = n.r if i == 'R' else n.l # else i == 'L'
        if nn == 'ZZZ':
            break
        ii = (ii + 1) % len(instr)

    return step

def do1():
    assert 2 == part1(ftest)
    assert 6 == part1(ftest2)
    assert 17263 == part1(finput)
