## Solution 1
def missing_number(nums):
    n = len(nums) + 1
    arr = [i for i in range(0, n)]
    element = set(arr) - set(nums)
    elem = list(element)[0]
    return elem


array = [3, 1, 5, 4, 2]
print(missing_number(array))