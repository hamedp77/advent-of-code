import re

pattern = re.compile(
       r'(four|eight|(?:fiv|(?:ni|o)n)e|t(?:wo|hree)|s(?:ix|even))|(\d)',
       re.IGNORECASE
       )


def word_to_digit(s: str) -> str | None:
    d = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    return d.get(s.lower())


def find_first(s: str) -> str | None:
    try:
        match = re.findall(pattern, s)[0]
    except IndexError:
        return ''
    word, digit = match
    if word:
        return word_to_digit(word)
    return digit


def find_last(s: str) -> str | None:
    temp = ''
    while True:
        temp = s[-1] + temp
        s = s[:-1]
        if find_first(temp):
            return find_first(temp)


with open('../input.txt', 'r') as f:
    total = 0

    for line in f:
        first = find_first(line)
        last = find_last(line)
        num = int(first + last)
        total += num

print(total)
