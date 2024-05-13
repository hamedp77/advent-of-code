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


with open('../input.txt', 'r') as f:
    total = 0

    for line in f:
        match = re.findall(pattern, line)[0]
        word, digit = match
        if word:
            first: str | None = word_to_digit(word)
        elif digit:
            first = digit

        second = ''
        temp = ''
        while not second:
            temp = line[-1] + temp
            line = line[:-1]
            if re.match(pattern, temp):
                match = re.findall(pattern, temp)[0]
                word, digit = match
                if word:
                    second: str | None = word_to_digit(word)
                elif digit:
                    second = digit
        num = int(first + second)
        total += num

print(total)
