from collections import Counter
from collections import deque


def calculate_points(file_name: str) -> int:
    with open(file_name) as f:
        lines = f.readlines()

    total_points = 0
    for line in lines:
        _, numbers = line.split(':')
        winning_numbers, my_numbers = numbers.split('|')
        winning_numbers = set(map(int, winning_numbers.split()))
        my_numbers = set(map(int, my_numbers.split()))

        matches = winning_numbers & my_numbers
        if matches:
            points = 2 ** (len(matches) - 1)
            total_points += points

    return total_points


def calculate_total_cards(file_name: str) -> int:
    with open(file_name) as f:
        lines = f.readlines()

    total_cards = 0
    cards = deque(range(1, len(lines) + 1))
    while cards:
        i = cards.popleft()
        line = lines[i - 1]
        _, numbers = line.split(':')
        winning_numbers, my_numbers = numbers.split('|')

        winning_numbers = Counter(map(int, winning_numbers.split()))
        my_numbers = Counter(map(int, my_numbers.split()))

        # Count matching occurrences
        matches = sum((winning_numbers & my_numbers).values())
        total_cards += 1

        if matches == 0:
            continue
        card_number = i + 1
        # Add copies of the next cards to the queue
        for _ in range(matches):
            if card_number < len(lines) + 1:
                cards.append(card_number)
                card_number += 1

    return total_cards


print(calculate_points('test.txt'))
print(calculate_points('day_four.txt'))
print(calculate_total_cards('test.txt'))
print(calculate_total_cards('day_four.txt'))
