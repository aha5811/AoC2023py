import utils
import os.path
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day19_test.txt')
finput = os.path.join(dir, 'day19_input.txt')

class Part:
    def __init__(self, line):
        self.kv = {} # key -> value
        # {x=787,m=2655,a=1222,s=2876}
        for kv in line[1:-1].split(','):
            k, v = kv.split('=')
            self.kv[k] = int(v)

    def __str__(self):
        return str(self.kv)


class Rule:
    def __init__(self, s: str):
        self.what = None
        self.gt = None # is greater than (or lesser than)
        self.v = None # value
        self.where = None
        # "a<2006:qkq" or just "qkq"
        if ':' in s:
            ss = s.split(':')
            self.what = ss[0][0]
            self.gt = ss[0][1] == '>'
            self.v = int(ss[0][2:])
            self.where = ss[1]
        else:
            self.where = s

    def __str__(self):
        return (
            (str(self.what) + ('>' if self.gt else '<') + str(self.v)
                if self.what is not None
                else 'True')
            + '->' + self.where)

    def target(self, p: Part) -> str:
        if self.what is None:
            return self.where
        else:
            pv = p.kv[self.what]
            return (
                self.where
                if self.gt and pv > self.v
                   or not self.gt and pv < self.v
                else None)


class Workflow:
    def __init__(self, line: str):
        # px{a<2006:qkq,m>2090:A,rfg}
        n_rules = line[:-1].split('{')
        self.n = n_rules[0]
        self.rules = []
        for rule in n_rules[1].split(','):
            self.rules.append(Rule(rule))

    def __str__(self):
        return self.n + ':' + str([str(rule) for rule in self.rules])

    def send(self, p: Part) -> str:
        for rule in self.rules:
            t = rule.target(p)
            if t is not None:
                return t

@utils.timeit
def part1(fname):
    res = 0

    wfm = {} # workflow name -> workflow
    ps = [] # parts

    for line in utils.f2lines(fname):
        if line.startswith('{'):
            ps.append(Part(line))
        elif '{' in line:
            wf = Workflow(line)
            wfm[wf.n] = wf

    for p in ps:
        if accept(wfm, p):
            res += sum(p.kv.values())

    return res

def accept(wfm, p: Part) -> bool:
    wfn = 'in' # workflow name
    while True:
        wfn = wfm[wfn].send(p)
        if wfn == 'A':
            return True
        elif wfn == 'R':
            return False

def do1():
    assert 19114 == part1(ftest)
    assert 476889 == part1(finput)
