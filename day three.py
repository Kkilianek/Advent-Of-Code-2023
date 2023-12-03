def calculate_parts_sum(file_name):
    with open(file_name, 'r') as f:
        data = [list(x.strip()) for x in f.readlines()]

    directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    parts_sum = 0
    non_symbols = ['.', ' ', '\n', '\t', '', '\r', '\v', '\f']

    for row in range(len(data)):
        col = 0
        while col < len(data[row]):
            if data[row][col].isdigit():
                num = []
                j = col
                while j < len(data[row]) and data[row][j].isdigit():
                    num.append(data[row][j])
                    j += 1
                num = int(''.join(num))

                added = False
                for dx, dy in directions:
                    for k in range(col, j):
                        x, y = row + dx, k + dy
                        if x in range(len(data)) and y in range(len(data[row])) and \
                                data[x][y].isascii() and not data[x][y].isdigit() and \
                                data[x][y] not in non_symbols:
                            parts_sum += num
                            added = True
                            break
                    if added:
                        break
                col = j
            else:
                col += 1
    return parts_sum


def calculate_gear_ratios(file_name):
    with open(file_name, 'r') as f:
        data = [list(line.strip()) for line in f]

    sum_ratios = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            # If the current character is a '*'
            if data[i][j] == '*':
                # Check all surrounding characters for exactly two numbers
                numbers = []
                added_numbers = set()
                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        if 0 <= i + di < len(data) and 0 <= j + dj < len(
                                data[i + di]) and data[i + di][j + dj].isdigit():
                            # Check for digits to the left
                            k = j + dj
                            while k > 0 and data[i + di][k - 1].isdigit():
                                k -= 1
                            # Check for digits to the right
                            l = j + dj
                            while l < len(data[i + di]) - 1 and data[i + di][
                                l + 1].isdigit():
                                l += 1
                            num = int("".join(data[i + di][k:l + 1]))
                            if num not in added_numbers:
                                numbers.append(num)
                                added_numbers.add(num)
                            if len(numbers) == 2:
                                break
                    if len(numbers) == 2:
                        break
                if len(numbers) == 2:
                    sum_ratios += numbers[0] * numbers[1]

    return sum_ratios


print(calculate_parts_sum('test.txt'))
print(calculate_parts_sum('day_three.txt'))
print(calculate_gear_ratios('test.txt'))
print(calculate_gear_ratios('day_three.txt'))
