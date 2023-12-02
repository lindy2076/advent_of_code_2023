def get_first_digit(line: str) -> int | None:
    for s in line:
        if s.isnumeric():
            return int(s)
    return None


def get_calibration_number(line: str) -> int:
    return get_first_digit(line)*10 + get_first_digit(line[::-1])


calibrated_sum = 0

with open("1input", 'r') as f:
    while (line := f.readline()):
        calibrated_sum += get_calibration_number(line)

print(calibrated_sum)
