nums = [5, 7, 7, 8, 8, 10]
target = 8

## 2 pointers O(n) complexity
def searchRange(nums, target):
    start = 0
    end = len(nums) - 1
    count = 0

    for i in range(0, len(nums)):
        if target == nums[i]:
            start = i
            count += 1

    for i in range(len(nums) - 1, -1, -1):
        if target == nums[i]:
            end = i

    if count == 0:
        return [-1, -1]

    else:
        return [end, start]

letter = searchRange(nums, target)
print('Range: ' + str(letter))

## Binary Search method in a different file