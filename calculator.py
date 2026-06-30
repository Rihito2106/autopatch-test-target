    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
    if not nums:
        raise ValueError("Cannot calculate the average of an empty list.")
    total = 0
    for n in nums:
        total += n
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
