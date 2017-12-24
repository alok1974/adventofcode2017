sum_ = 0
with open('input.txt', 'r') as fp:
    for line in fp.readlines():
        line = map(int, line.split())
        sum_ += (max(line) - min(line))
print sum_
