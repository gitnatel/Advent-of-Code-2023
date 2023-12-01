f = open("01/input.txt")

f.seek(0)

lines=[]
calibration=[]

for line in f:
    stripped_line = line.strip()
    if stripped_line:
        lines.append(stripped_line)

f.close()

def convert_spelled_to_digit(word):
    number_words = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    return number_words.get(word.lower(), word)

def convert_mixed_strings(strings):
    result = []
    for string in strings:
        words = string.split()
        modified_words = [convert_spelled_to_digit(word) for word in words]
        converted_string = "".join(map(str, modified_words))
        result.append(converted_string)

    return result

converted_lines = convert_mixed_strings(lines)

for line in converted_lines:
    first_digit_index = None
    for i, char in enumerate(line):
        if char.isdigit():
            first_digit_index = i
            break

    last_digit_index = None
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            last_digit_index = i
            break

    if first_digit_index is not None and last_digit_index is not None:
        first_digit = int(line[first_digit_index])
        last_digit = int(line[last_digit_index])
        calibration.append(first_digit * 10 + last_digit)

ans = sum(calibration)

print(ans)