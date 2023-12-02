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
    
    def set_power(self) -> int:
        min_red, min_green, min_blue = 0, 0, 0
        for round in self.rounds:
            min_red = max(min_red, round.r)
            min_green = max(min_green, round.g)
            min_blue = max(min_blue, round.b)
        return min_red * min_green * min_blue

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


power_sum = 0

with open("input_1", 'r') as f:
    while (line := f.readline()):
        game = Game.parse_line(line)
        power_sum += game.set_power()

print(power_sum)
