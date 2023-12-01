import re


def sum_calibration_values(file_path: str) -> int:
    with open(file_path) as file:
        lines = file.readlines()

    total_sum = 0
    for line in lines:
        digits = re.findall('\d', line)
        if digits:
            total_sum += int(digits[0] + digits[-1])

    return total_sum


def sum_calibration_values_updated(file_path: str) -> int:
    with open(file_path) as file:
        lines = file.readlines()

    total_sum = 0
    digits_and_words = '1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine'
    replacement_dict = {n: str(i % 9 + 1) for i, n in
                        enumerate(digits_and_words.split('|'))}

    for line in lines:
        digit_list = [*map(replacement_dict.get,
                           re.findall(rf'(?=({digits_and_words}))', line)
                           )]
        if digit_list:
            # create a number from the first digit and the last digit in the line
            number = int(digit_list[0] + digit_list[-1])
            total_sum += number

    return total_sum


# print(sum_calibration_values('day_one.txt'))
print(sum_calibration_values_updated('test.txt'))
print(sum_calibration_values_updated('day_one.txt'))
