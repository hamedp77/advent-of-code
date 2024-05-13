def find_first_digit(s: str) -> str:
    for c in s:
        if c.isdigit():
            return c
    return ''


def find_last_digit(s: str) -> str:
    for c in s[::-1]:
        if c.isdigit():
            return c
    return ''


with open('../input.txt', 'r') as f:
    total = 0
    for line in f:
        first = find_first_digit(line)
        last = find_last_digit(line)
        num = int(first + last)
        total += num

print(total)
