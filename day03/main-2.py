import sys
import re
from math import prod

with open(sys.argv[1], 'r') as f:
    data = f.read()

pairs= re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', data)
s=sum(prod(list(map(int, x))) for x in pairs)


enable=True
s=0
s2=0
for condition in re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", data):
    match condition:
        case "do()":
            enable=True
        case "don't()":
            enable=False
        case _:
            x1,x2=map(int, condition[4:-1].split(','))
            s=s+(x1*x2)
            if enable:
                s2=s2+(x1*x2)

print(f'Answer1: {s}')
print(f'Answer2: {s2}')