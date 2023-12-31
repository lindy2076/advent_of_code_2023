def predict_next(nums: list[int]) -> int:
    diffs = [y - x for x, y in zip(nums, nums[1:])]
    for x in nums:
        if x != 0:
            return nums[0] - predict_next(diffs)
    return 0


def parse_nums(line: str) -> list[int]:
    return list(map(int, line.strip().split()))


for filename in ["9_test", "9_input"]:
    
    prediction_sum = 0
    with open(filename, 'r') as f:
        while (line := f.readline()):
            prediction_sum += predict_next(parse_nums(line))
    print(prediction_sum)
