import utils
from collections import Counter
import functools
import os.path
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day07_test.txt')
finput = os.path.join(dir, 'day07_input.txt')

cart_order = [ 'A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2' ]

class Hand:
    def __init__(self, s):
        cb = s.split(' ')
        self.cards = cb[0]
        self.bid = int(cb[1])
        c = Counter(self.cards).most_common(2) # 55443 -> [('5', 2'), ('4', 2)]
        # self made rank: 5 = 50, 4 = 40, 3+2 = 32, 3 = 30, 2+2 = 22, 2 = 20, 1 = 10
        self.rank = c[0][1] * 10 + (c[1][1] if len(c) > 1 and c[1][1] > 1 else 0)

    def __str__(self):
        return ''.join(self.cards) + ' ' + str(self.bid) + ' ' + str(self.rank)

def hand_cmp(h1, h2):
    if h1.rank != h2.rank:
        return h1.rank - h2.rank
    else: # check rank of cards in order
        for n in range(len(h1.cards)):
            cmp = cart_order.index(h2.cards[n]) - cart_order.index(h1.cards[n])
            if cmp != 0:
                return cmp
        return 0

@utils.timeit
def part1(fname):

    hands = []
    for line in utils.f2lines(fname):
        hands.append(Hand(line))
    hands.sort(key=functools.cmp_to_key(hand_cmp))

    res = 0
    n = 1
    for h in hands:
        res += h.bid * n
        n += 1

    return res

def do1():
    assert 6440 == part1(ftest)
    assert 249638405 == part1(finput)
