from functools import reduce


def how_many_ways_for_one(time: int, distance: int) -> int:
    num_ways = 0
    for hold_time in range(time):
        if (time - hold_time) * hold_time > distance:
            num_ways += 1
    return num_ways


def how_many_ways_for_all(time_list: list[int], distance_list: list[int]) -> list[int]:
    values = []
    for t, d in zip(time_list, distance_list):
        values.append(how_many_ways_for_one(t, d))

    return values


def prod(list_: list[int]) -> int:
    return reduce(lambda x, y: x * y, list_)


def get_values(line: str) -> tuple[int]:
    return [int(x) for x in line.split(":")[1].split()]


for filename in ["6_test", "6_input"]:
    with open(filename, 'r') as f:
        t_line = f.readline().strip()
        d_line = f.readline().strip()

    t, d = get_values(t_line), get_values(d_line)
    print(prod(how_many_ways_for_all(t, d)))
