f = open("01/input.txt")

f.seek(0)

lines=[]
calibration=[]

for line in f:
    stripped_line = line.strip()
    if stripped_line:
        lines.append(stripped_line)

f.close()

for line in lines:
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