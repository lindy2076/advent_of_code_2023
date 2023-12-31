class GameRound:
    def __init__(self, r: int = 0, g: int = 0, b: int = 0) -> None:
        self.r = r
        self.g = g
        self.b = b

    def __gt__(self, obj) -> bool:
        return self.r > obj.r or self.g > obj.g or self.b > obj.b
    
    def __repr__(self) -> str:
        return f"r: {self.r}, g: {self.g}, b: {self.b}"
    
    @staticmethod
    def parse_from_line(line: str) -> 'GameRound':
        colors = {"red": 0, "green": 0, "blue": 0}
        for set_ in line.split(","):
            amount, color = set_.strip().split(" ")
            colors[color] += int(amount)
        return GameRound(colors["red"], colors["green"], colors["blue"])


class Game:
    def __init__(self, id: int, rounds: list[GameRound]):
        self.id = id
        self.rounds = rounds

    def is_possible(self, maxAmount: GameRound):
        for round in self.rounds:
            if round > maxAmount:
                return False
        return True
    
    def __str__(self) -> str:
        r = """"""
        r += (f"game_id: {self.id}\n")
        for round in self.rounds:
            r += (f"\t{round}")
        return r

    @staticmethod
    def parse_line(line: str) -> 'Game':
        game_id, rounds = line.split(":")
        game_id = int(game_id[4:])
        game_rounds = []
        for round in rounds.split(";"):
            game_round = GameRound.parse_from_line(round.strip())
            game_rounds.append(game_round)
        return Game(game_id, game_rounds)


MAX_AMOUNT = GameRound(12, 13, 14)

ID_sum = 0

with open("test_1", 'r') as f:
    while (line := f.readline()):
        game = Game.parse_line(line)
        if game.is_possible(MAX_AMOUNT):
            ID_sum += game.id

print(ID_sum)
