NOT_THE_SYMBOLS = set([x for x in map(str, range(10))] + ["."])


def line_to_char_list(line: str) -> list[str]:
    return [s for s in line.strip()]


def get_numbers_and_pos(line: str) -> list[int, int, int]:
    """retrieve numbers with their left and right indexes"""
    l = 0
    n = len(line)
    nums_and_pos = []
    while (l < n):
        next_num = ""
        num_l = l
        while (line[l].isnumeric()):
            next_num += line[l]
            if l == n - 1:
                break    
            l += 1
        if next_num:
            nums_and_pos.append([int(next_num), num_l, l - 1])
        l += 1
    return nums_and_pos


def check_substring_contains_special(substr: str):
    for s in substr:
        if s not in NOT_THE_SYMBOLS:
            return True
    return False


def get_special_nums_in_line(line_num: int, table: list[list[str]]) -> list[int]:
    special_nums = []
    line = table[line_num]
    n = len(line)
    numbers_and_pos = get_numbers_and_pos(line)
    
    for number, l, r in numbers_and_pos:
        left_special = (l > 0 and line[l - 1] not in NOT_THE_SYMBOLS)
        right_special = (r < n - 1 and line[r + 1] not in NOT_THE_SYMBOLS)
        top_special = False
        bottom_special = False

        if not (left_special or right_special):
            if l > 0:
                l -= 1
            if r < n - 1:
                r += 1

            if line_num > 0:
                top_special = check_substring_contains_special(table[line_num - 1][l:r + 1])
            if line_num < n - 1:
                bottom_special = check_substring_contains_special(table[line_num + 1][l:r + 1])

        if left_special or right_special or top_special or bottom_special:
            special_nums.append(number)
            continue
    return special_nums


def get_special_nums_in_table(table: list[list[str]]) -> list[list[int]]:
    lines = []
    for line_num, _ in enumerate(table):
        lines.append(get_special_nums_in_line(line_num, table))
    return lines


def get_sum_of_special_nums(table: list[list[str]]) -> int:
    return sum([sum(line) for line in get_special_nums_in_table(table)])


def get_table_from_file(filename: str) -> list[list[str]]:
    lines_table = []
    with open(filename, 'r') as f:
        while (line := f.readline()):
            lines_table.append(line_to_char_list(line))
    return lines_table


for filename in ("3_test", "3_input"):
    table = get_table_from_file(filename)
    print(get_sum_of_special_nums(table))
