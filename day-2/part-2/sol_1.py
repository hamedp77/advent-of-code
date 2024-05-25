import re

INPUT_FILE = '../input.txt'
DEBUG_FILE = '../short_input.txt'

COLORS = ('red', 'green', 'blue')


def get_max_cube_count(s: str, color: str) -> int:
    pattern = re.compile(rf'(\d+) ({color})', re.IGNORECASE)
    if not re.search(pattern, s):
        return 0
    max_val = max([int(count) for count, _ in re.findall(pattern, s)])

    return max_val


def main() -> int:
    powers = []
    with open(INPUT_FILE, 'r') as f:
        for game in f:
            least_cubes = []
            this_game_power = 1

            for color in COLORS:
                max_count = get_max_cube_count(game, color)
                least_cubes.append(max_count)

            for count in least_cubes:
                this_game_power *= count
            powers.append(this_game_power)

    total_powers = sum(powers)
    print(total_powers)

    return 0


if __name__ == '__main__':
    exit(main())
