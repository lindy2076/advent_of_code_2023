class Card:
    def __init__(self, line: str, card_dict: dict):
        card_num, nums = line.split(":")
        card_id = int(card_num.strip().split()[1])
        winning_nums_s, player_nums_s = nums.strip().split("|")
        winning_nums = set(map(int, winning_nums_s.split()))
        player_nums = set(map(int, player_nums_s.split()))

        copies = 1
        if card_id in card_dict:
            copies += card_dict[card_id]
        card_dict[card_id] = copies

        self.id = card_id
        self.winning_nums = winning_nums
        self.player_nums = player_nums
        self.copies = copies
        self.proceed_copies(card_dict)

    def __repr__(self):
        return "id: {0}, winning_nums: {1}, player_nums: {2}".format(
            self.id,
            ' '.join(map(str, self.winning_nums)),
            ' '.join(map(str, self.player_nums))
        )

    def proceed_copies(self, card_dict):
        """"""
        copies_to_make = self.copies
        cards_to_copy = 0

        for num in self.player_nums:
            if num in self.winning_nums:
                cards_to_copy += 1

        for i in range(self.id, self.id + cards_to_copy):
            if (i + 1) not in card_dict:
                card_dict[i + 1] = 0
            card_dict[i + 1] += copies_to_make


def main():
    for filename in ["test_4", "input_4"]:
        cards = {}
        with open(filename, 'r') as f:
            while (line := f.readline()):
                card = Card(line, cards)
        print(sum(cards.values()))


main()
