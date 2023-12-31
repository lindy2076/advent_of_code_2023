digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0}

def get_first_digit(line: str) -> int | None:
    for idx, s in enumerate(line):
        if s.isnumeric():
            return int(s)
        if line[idx: idx + 3] in digits:
            return digits[line[idx: idx + 3]]
        if line[idx: idx + 4] in digits:
            return digits[line[idx: idx + 4]]
        if line[idx: idx + 5] in digits:
            return digits[line[idx: idx + 5]]
    return None


def get_last_digit(line: str) -> int | None:
    n = len(line)
    for i in range(n):
        idx = n - i - 1
        s = line[idx]
        if s.isnumeric():
            return int(s)
        if line[idx - 2: idx + 1] in digits:
            return digits[line[idx - 2: idx + 1]]
        if line[idx - 3: idx + 1] in digits:
            return digits[line[idx - 3: idx + 1]]
        if line[idx - 4: idx + 1] in digits:
            return digits[line[idx - 4: idx + 1]]
    return None


def get_calibration_number(line: str) -> int:
    return get_first_digit(line) * 10 + get_last_digit(line)


calibrated_sum = 0

with open("1input", 'r') as f:
    while (line := f.readline()):
        calibrated_sum += get_calibration_number(line)

print(calibrated_sum)
