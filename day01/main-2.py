import sys

with open(sys.argv[1] , 'r') as f:
    lines = [list(map(int, line.split())) for line in f.readlines()]

list1, list2 =list(map(list, zip(*lines)))

part1=sum(x * len([y for y in list2 if y == x]) for x in list1)

print(f'Answer: {part1}')
