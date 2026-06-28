def divide(a, b):
    return a / b


def average(nums):
    total = 0
    for n in nums:
        total += n
    return total / len(nums)


def find_max(nums):
    max_val = nums[0]
    for n in nums:
        if n > max_val:
            max_val = n
    return max_val
