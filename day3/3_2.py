class NumberAndPos:
    def __init__(self, num: int, l: int, r: int):
        self.l = l
        self.r = r
        self.num = num
        self.used = False

    def __repr__(self):
        return str(self.num)


def line_to_char_list(line: str) -> list[str]:
    return [s for s in line.strip()]


def get_numbers_and_pos(line: str) -> list[NumberAndPos]:
    """retrieve numbers with their left and right indexes"""
    l = 0
    n = len(line)
    nums_and_pos = []
    while (l < n):
        next_num = ""
        num_l = l
        while (line[l].isnumeric()):
            next_num += line[l]
            l += 1
            if l == n:
                break    
        if next_num:
            nums_and_pos.append(NumberAndPos(int(next_num), num_l, l - 1))
        l += 1
    return nums_and_pos


def map_numbers_to_table(table: list[list[str]]) -> list[list[None | NumberAndPos]]:
    """returns a table where each cell is a link to a number that has one digit in the cell"""
    new_table = []
    line_len = len(table[0])
    for _, line in enumerate(table):
        new_line = []
        for num_and_pos in get_numbers_and_pos(line):
            new_line += [None] * (num_and_pos.l - len(new_line))
            new_line += [num_and_pos] * (num_and_pos.r - num_and_pos.l + 1)
        new_line += [None] * (line_len - len(new_line))
        new_table.append(new_line)
    return new_table


def get_all_gear_ratios(table: list[list[str]], mapped_nums: list[list[None | NumberAndPos]]) -> list[list[int]]:
    ratios = []
    n = len(table[0])
    for i, line in enumerate(table):
        line_ratios = []
        for j, s in enumerate(line):
            if s != "*":
                continue
            to_scan = []
            to_prod = []
            if i > 0:
                to_scan.append((i - 1, j))
            if j > 0:
                to_scan.append((i, j - 1))
            if i > 0 and j > 0:
                to_scan.append((i - 1, j - 1))
            if i < n - 1:
                to_scan.append((i + 1, j))
            if j < len(table) - 1:
                to_scan.append((i, j + 1))
            if i < n - 1 and j < len(table) - 1:
                to_scan.append((i + 1, j + 1))
            if i > 0 and j < len(table) - 1:
                to_scan.append((i - 1, j + 1))
            if i < n - 1 and j > 0:
                to_scan.append((i + 1, j - 1))
            for (i_, j_) in to_scan:
                num_and_pos = mapped_nums[i_][j_]
                if (num_and_pos is not None) and not num_and_pos.used:
                    to_prod.append(num_and_pos)
                    num_and_pos.used = True

            if len(to_prod) == 2:
                line_ratios.append(to_prod[0].num * to_prod[1].num)
            for num in to_prod:
                num.used = False

        ratios.append(line_ratios)
    return ratios


def get_sum_of_all_gear_ratios(table: list[list[str]]) -> int:
    mapped_nums = map_numbers_to_table(table)
    return sum([sum(line) for line in get_all_gear_ratios(table, mapped_nums)])


def get_table_from_file(filename: str) -> list[list[str]]:
    lines_table = []
    with open(filename, 'r') as f:
        while (line := f.readline()):
            lines_table.append(line_to_char_list(line))
    return lines_table


for filename in ["3_test", "3_input"]:
    table = get_table_from_file(filename)
    print(get_sum_of_all_gear_ratios(table))
