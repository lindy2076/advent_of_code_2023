def is_instruction(line: str) -> bool:
    if "(" in line:
        return False
    return True


def parse_node(line: str) -> tuple[str, str, str]:
    return line.replace("=", "").replace("(", "").replace(")", "").replace(",", "").strip().split()


for filename in ["8_test_1", "8_test_2", "8_input"]:
    nodes = {}
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
    steps = 0
    curr_node = "AAA"
    while (curr_node != "ZZZ"):
        next_turn = int(instructions[steps % len(instructions)])
        curr_node = nodes[curr_node][next_turn] 
        steps += 1
    
    print(steps)