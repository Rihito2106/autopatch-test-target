def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def average(nums):
    total = 0
    for n in nums:
        total += n
    if not nums:
        raise ZeroDivisionError("Cannot calculate average of an empty list.")
    return total / len(nums)


def find_max(nums):
    max_val = nums[0]
    for n in nums:
        if n > max_val:
            max_val = n
    return max_val
