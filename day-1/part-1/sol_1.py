with open('../input.txt', 'r') as f:
    total = 0
    for line in f:
        first_num = ''
        second_num = ''

        for c in line:
            try:
                int(c)
            except ValueError:
                continue

            num = c
            if not first_num:
                first_num += num
            else:
                second_num = ''
                second_num += num

        if not second_num:
            second_num = first_num

        combined_num = int(first_num + second_num)
        total += combined_num

print(total)
