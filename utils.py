from functools import wraps
import time

def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'{func.__name__}{args} took {total_time:.4f}s')
        return result
    return timeit_wrapper

def f2lines(fname):
    res = []
    with open(fname, 'r') as file:
        for line in file:
            res.append(line.strip())
    return res
