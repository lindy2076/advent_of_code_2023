def is_instruction(line: str) -> bool:
    if "(" in line:
        return False
    return True


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(nums: list) -> int:
    res = 1
    for n in nums:
        res = res * n // gcd(res, n)
    return res


def parse_node(line: str) -> tuple[str, str, str]:
    return line.replace("=", "").replace("(", "").replace(")", "").replace(",", "").strip().split()


for filename in ["8_test_3", "8_input"]:
    nodes = {}
    starting_nodes = []
    with open(filename, 'r') as f:
        while (line := f.readline()):
            line = line.strip()
            if not line:
                continue

            if is_instruction(line):
                instructions = line.replace("R", "1").replace("L", "0").strip()
                continue

            curr, l, r = parse_node(line)
            nodes[curr] = (l, r)
            if curr[-1] == "A":
                starting_nodes.append(curr)

    steps = []
    print(starting_nodes)
    for node_ in starting_nodes:
        k = 0
        curr_node = node_
        while (curr_node[-1] != "Z"):
            next_turn = int(instructions[k % len(instructions)])
            curr_node = nodes[curr_node][next_turn] 
            k += 1
        
        steps.append(k)
    print(lcm(steps))
