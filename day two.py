def parse_file(file_path: str) -> list:
    parsed_data = []

    with open(file_path) as file:
        input_data = file.readlines()

    for line in input_data:
        line = line.strip()

        if not line:
            continue

        game_id, *set_data = line.split(': ')
        game_id = int(game_id.split(' ')[1])
        sets = set_data[0].split('; ')

        color_counts = [set.split(', ') for set in sets]
        color_counts = [{color: int(num) for num, color in
                         (count.split(' ') for count in color_set)} for color_set in
                        color_counts]

        parsed_data.append((game_id, color_counts))

    return parsed_data


def possible_games(file_path: str) -> int:
    game_data = parse_file(file_path)
    possible_game_ids_sum = 0
    bag = {'red': 12, 'green': 13, 'blue': 14}

    for game_id, color_counts in game_data:
        possible = all(
            count.get(color, 0) <= bag[color] for count in color_counts for color in
            bag)

        if possible:
            possible_game_ids_sum += game_id

    return possible_game_ids_sum


def minimum_cubes_power(file_path: str) -> int:
    game_data = parse_file(file_path)
    total_power = 0

    for _, color_counts in game_data:
        min_cubes = {'red': 0, 'green': 0, 'blue': 0}

        for count in color_counts:
            for color in min_cubes:
                min_cubes[color] = max(min_cubes[color], count.get(color, 0))

        power = min_cubes['red'] * min_cubes['green'] * min_cubes['blue']
        total_power += power

    return total_power

print(possible_games('test.txt'))
print(possible_games('day_two.txt'))
print(minimum_cubes_power('test.txt'))
print(minimum_cubes_power('day_two.txt'))
