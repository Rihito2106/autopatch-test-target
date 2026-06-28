def divide(a, b):
    if b == 0:
        return None
    return a / b
    if not nums:
        return None
    total = 0
    for n in nums:
        total += n
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
