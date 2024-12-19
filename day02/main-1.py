import sys

def part1(line:str)->bool:
    nums =list(map(int, line.split(' '))) 
    diff=[abs(x1-x2) for x1, x2 in zip(nums, nums[1:])]
    if not all (1<=d<=3 for d in diff):
        return False
    if not all(x1<x2 for x1, x2 in zip(nums, nums[1:])):
        if not all(x1>x2 for x1, x2 in zip(nums, nums[1:])):
            return False
    return True




with open(sys.argv[1], 'r') as f:
    lines = f.readlines()   

safe=[r for r in lines if part1(r)]

print(f'Answer: {len(safe)}')