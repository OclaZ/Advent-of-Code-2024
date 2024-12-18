import sys

with open(sys.argv[1] , 'r') as f:
    lines = [list(map(int, line.split())) for line in f.readlines()]

list1, list2 =list(map(list, zip(*lines)))

solution=sum(abs(x1-x2) for x1, x2 in zip(sorted(list1), sorted(list2)))

print(f'Answer: {solution}')
