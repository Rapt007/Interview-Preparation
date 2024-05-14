
nums = [-1, 0, 3, 5, 9, 12]
target = 10

# Ceiling of a number is the smallest number that is equal to or bigger than the target.
def CeilingNumber(nums, target):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = start + int((end-start) / 2)
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            start = mid + 1
        else:
            end = mid - 1

    else:
        return start


index = CeilingNumber(nums, target)
print('Ceiling of a number: ' + str(nums[index]))