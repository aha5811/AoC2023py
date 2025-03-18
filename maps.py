import utils

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'

    def __eq__(self, other):
        if isinstance(other, Pos):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash(str(self))

class Map:
    def from_file(fname):
        """ returns Map """
        return Map(utils.f2lines(fname))

    def __init__(self, lines):
        self.rows = [list(line.strip()) for line in lines]
        self.h: int = len(self.rows)
        self.w: int = len(self.rows[0])

    def __str__(self):
        res = ''
        for row in self.rows:
            res += '\n' + ''.join(row)
        return res[1:]

    def get(self, x: int, y: int) -> str:
        return (
            None
            if x < 0 or x >= self.w or y < 0 or y >= self.h
            else self.rows[y][x])

    def set(self, x: int, y: int, c: str):
        if self.get(x, y) is not None:
            self.rows[y][x] = c

    def get_symbols(self) -> list[str]:
        res = set()
        for x in range(self.w):
            for y in range(self.h):
                res.add(self.get(x, y))
        return list(res)

    def find_all(self, s: str) -> list[Pos]:
        res = []
        for x in range(self.w):
            for y in range(self.h):
                if self.get(x, y) == s:
                    res.append(Pos(x, y))
        return res
