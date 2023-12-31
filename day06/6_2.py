def how_many_ways_for_one(time: int, distance: int) -> int:
    num_ways = 0
    for hold_time in range(time):
        if (time - hold_time) * hold_time > distance:
            num_ways += 1
    return num_ways


def get_value(line: str) -> int:
    return int("".join(line.split(":")[1].split()))


for filename in ["6_test", "6_input"]:
    with open(filename, 'r') as f:
        t_line = f.readline().strip()
        d_line = f.readline().strip()

    t, d = get_value(t_line), get_value(d_line)
    print(how_many_ways_for_one(t, d))
