import sys

def safe(nums: list[int]) -> bool:
    diff = [abs(x1 - x2) for x1, x2 in zip(nums, nums[1:])]
    if not all(1 <= d <= 3 for d in diff):
        return False
    if not all(x1 < x2 for x1, x2 in zip(nums, nums[1:])):
        if not all(x1 > x2 for x1, x2 in zip(nums, nums[1:])):
            return False
    return True

def safe1(line: str) -> bool:
    nums = list(map(int, line.split()))
    return safe(nums)

def safe2(line: str) -> bool:
    nums = list(map(int, line.split()))
    if safe(nums): 
        return True
    for i in range(len(nums)):
        new_nums = nums[:i] + nums[i + 1:]
        if safe(new_nums): 
            return True
    return False

with open(sys.argv[1], 'r') as f:
    lines = f.read().strip().split('\n')

part1 = [r for r in lines if safe1(r)]
part2 = [r for r in lines if safe2(r)]

print(f'Answer 1: {len(part1)}')
print(f'Answer 2: {len(part2)}')
