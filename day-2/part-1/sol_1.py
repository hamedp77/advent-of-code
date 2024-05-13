import re

INPUT_FILE = '../input.txt'
DEBUG_FILE = '../short_input.txt'

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def get_game_id(s: str) -> int:
    pattern = re.compile(r'\d+')
    try:
        match = re.findall(pattern, s)[0]
        game_id = int(match)
    except IndexError:
        return -1

    return game_id


def get_cube_count(s: str, color: str) -> int:
    pattern = re.compile(rf'(\d+) ({color})', re.IGNORECASE)
    if not re.search(pattern, s):
        return 0
    total = sum([int(count) for count, _ in re.findall(pattern, s)])

    return total


def is_valid_set(red_count: int, green_count: int, blue_count: int) -> bool:
    if red_count > MAX_RED:
        return False
    if green_count > MAX_GREEN:
        return False
    if blue_count > MAX_BLUE:
        return False
    return True


def main() -> int:
    with open(INPUT_FILE, 'r') as f:
        valid_games = []
        for game in f:
            game_id = get_game_id(game)
            prefix = f'Game {game_id}: '
            stripped_game = game.removeprefix(prefix)
            sets = stripped_game.split(';')

            for set_ in sets:
                reds = get_cube_count(set_, 'red')
                greens = get_cube_count(set_, 'green')
                blues = get_cube_count(set_, 'blue')

                if not is_valid_set(reds, greens, blues):
                    break
            else:
                valid_games.append(game_id)

    total = sum(valid_games)
    print(total)

    return 0


if __name__ == '__main__':
    exit(main())
