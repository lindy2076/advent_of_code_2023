class LineType():
    SEEDS = "seeds"
    MAP = "map"
    NUM_RANGE = "num_range"
    UNDEFINED = "undefined"


class Map():
    def __init__(self, name: str):
        self.name = name
        self.mapa = []

    def add_kvr(self, kvr_tuple: tuple[int]):
        self.mapa.append(kvr_tuple)

    def maps_from(self) -> str:
        return self.name.split("-")[0]

    def maps_to(self) -> str:
        return self.name.split("-")[-1]

    def get_value(self, key: int):
        for v, k, r in self.mapa:
            if key >= k and key <= k + r - 1:
                return v + key - k
        return key


class LineProcessor():
    def __init__(self, line: str):
        self.line = line.lower().strip()

    def line_type(self) -> LineType:
        if "map" in self.line:
            return LineType.MAP
        if "seeds" in self.line:
            return LineType.SEEDS
        if self.line.replace(" ", "").isnumeric():
            return LineType.NUM_RANGE
        return LineType.UNDEFINED

    def get_seeds(self) -> set[int]:
        """requires self.line to be LineType.SEEDS"""
        return set(map(int, self.line.split(":")[1].strip().split(" ")))

    def get_map_name(self) -> str:
        """requires self.line to be LineType.MAP"""
        return self.line.split(" ")[0].strip()

    def get_kvr(self):
        return tuple(map(int, self.line.split(" ")))

    def __repr__(self) -> str:
        return f"{self.line_type()}: {self.line}"


class GardenHelper():
    def __init__(self, ):
        ...


for filename in ["5_test", "5_input"]:
    with open(filename, 'r') as f:
        maps = {}
        new_map = None
        while (line := f.readline()):
            lp = LineProcessor(line)
            match lp.line_type():
                case LineType.SEEDS:
                    seeds = lp.get_seeds()
                case LineType.MAP:
                    if new_map is not None:
                        maps[new_map.maps_from()] = new_map
                    new_map = Map(lp.get_map_name())
                case LineType.NUM_RANGE:
                    new_map.add_kvr(lp.get_kvr())
        if new_map is not None:
            maps[new_map.maps_from()] = new_map


        locations = {}
        for seed in seeds:
            # print("SEED NUMBER", seed)
            curr_key = seed
            map_ = maps["seed"]
            while (map_.maps_to() != "location"):
                # print(curr_key, map_.maps_to(), map_.name)
                curr_key = map_.get_value(curr_key) 
                map_ = maps[map_.maps_to()]
            
            location = map_.get_value(curr_key)
            # print(location, map_.maps_to(), map_.name)
            locations[seed] = location 
        
        print(min(locations.values()))
