with open('../input.txt', 'r') as f:
    total = 0
    for line in f:
        nums = []

        for c in line:
            try:
                nums.append(int(c))
            except ValueError:
                continue
        first, last = nums[0], nums[-1]
        num = int(str(first) + str(last))
        total += num

print(total)
