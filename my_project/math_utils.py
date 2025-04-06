import statistics

# Return average
def average(nums):
    if not nums:
        return None
    return sum(nums) / len(nums)

# Return middle value
def median(nums):
    if not nums:
        return None
    return statistics.median(nums)

# Return the sample standard deviation
def stddev(nums):
    if not nums:
        return None
    return statistics.stdev(nums)

if __name__ == '__main__':
    print(average([1, 2, 3]))
    print(median([1, 2, 3]))
