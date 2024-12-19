import sys
import re
from math import prod

with open(sys.argv[1], 'r') as f:
    data = f.read()

pairs= re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', data)
s=sum(prod(list(map(int, x))) for x in pairs)

print(f'Answer: {s}')
