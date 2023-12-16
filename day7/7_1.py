CARD_VALUES = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9,
               "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}


class HandType:
    FIVE = 6
    FOUR = 5
    FULL_HOUSE = 4
    THREE = 3
    TWO_PAIR = 2
    PAIR = 1
    HIGH_CARD = 0


def hand_type(hand: str) -> HandType:
    cards = {}
    for c in hand:
        if c not in cards:
            cards[c] = 0
        cards[c] += 1

    cv = cards.values()
    if len(cards) == 1:
        return HandType.FIVE
    if len(cards) == 2:
        if 4 in cv:
            return HandType.FOUR
        return HandType.FULL_HOUSE
    if len(cards) == 3:
        if 3 in cv:
            return HandType.THREE
        return HandType.TWO_PAIR
    if len(cards) == 5:
        return HandType.HIGH_CARD
    return HandType.PAIR


def greater_hand_key(hand: str) -> tuple:
    return tuple([hand_type(hand)] + [CARD_VALUES[card] for card in hand])


def total_winnings(cards: list) -> int:
    s = 0
    for idx, hand in enumerate(cards):
        s += cards[hand] * (idx + 1)
    return s


for filename in ["7_test", "7_input"]:
    cards = {}
    with open(filename, 'r') as f:
        while (line := f.readline()):
            hand, bid = line.split()
            cards[hand] = int(bid)

    d = dict(sorted(cards.items(), key= lambda x: greater_hand_key(x[0]), reverse=False))
    print(total_winnings(d))
