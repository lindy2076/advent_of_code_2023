class Card:
    def __init__(self, line: str):
        card_num, nums = line.split(":")
        card_id = int(card_num.strip().split()[1])
        winning_nums_s, player_nums_s = nums.strip().split("|")
        winning_nums = set(map(int, winning_nums_s.split()))
        player_nums = set(map(int, player_nums_s.split()))

        self.id = card_id
        self.winning_nums = winning_nums
        self.player_nums = player_nums
    
    def __repr__(self):
        return "id: {0}, winning_nums: {1}, player_nums: {2}".format(
            self.id,
            ' '.join(map(str, self.winning_nums)),
            ' '.join(map(str, self.player_nums))
        )
    
    def get_score(self):
        score = 0
        for num in self.player_nums:
            if num in self.winning_nums:
                if score == 0:
                    score += 1
                else:
                    score *= 2
        return score


def main():
    for filename in ["test_4", "input_4"]:
        total_score = 0
        with open(filename, 'r') as f:
            while (line := f.readline()):
                card = Card(line)
                total_score += card.get_score()
        print(total_score)


main()
