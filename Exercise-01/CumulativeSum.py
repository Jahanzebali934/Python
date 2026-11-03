def cumulative_sum(n):
    """Calulate the cumulative sum of all integers from 1 to n"""
    total = 0
    for i in range(1,n+1):
        total += i
    return total
print("All tests passed!")
assert cumulative_sum(1) == 1
assert cumulative_sum(5) == 1 + 2 + 3 + 4 + 5
assert cumulative_sum(100) == 5050