from itertools import count


def exponential(round, start=0, increment=2, limit=None):
    limit_func = min if 0 < increment else max
    result = start + (increment ** round)
    return limit_func(result, limit) if limit else result

def exponential_generator(start=0, increment=2, limit=None):
    for round in count(0):
        yield exponential(round, start, increment, limit)

def exponential_sequence(start=0, increment=2, limit=None, count=1):
    generator = exponential_generator(start, increment, limit)
    return [next(generator) for _ in range(count)]


gen = exponential_generator()

assert next(gen) == exponential(0)
assert next(gen) == exponential(1)
assert next(gen) == exponential(2)

assert exponential_sequence(count=10) == [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
