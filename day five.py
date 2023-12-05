def map_seeds(filename, initial_seeds):
    with open(filename) as almanac:
        while True:
            line = almanac.readline().strip()

            def convert_number(mapping, num):
                for start_dest, start_source, length in mapping:
                    if start_source <= num < (start_source + length):
                        return start_dest + (num - start_source)

                return num

            if line == "":
                break

            else:
                map_line = almanac.readline().strip()

                mapping = []

                while map_line != "":
                    start_dest, start_source, length = map(int, map_line.split())
                    mapping.append((start_dest, start_source, length))

                    map_line = almanac.readline().strip()

                for i in range(len(initial_seeds)):
                    initial_seeds[i] = convert_number(mapping, initial_seeds[i])

    print(min(initial_seeds))


def get_seeds_from_file(filename):
    with open(filename) as almanac:
        seeds = list(map(int, almanac.readline().strip().split("seeds: ")[1].split()))
    return seeds


filename = "day_five.txt"
seeds = get_seeds_from_file(filename)
map_seeds(filename, seeds)
