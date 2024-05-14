
nums = [-1, 0, 3, 5, 9, 12]
target = 10

# Floor of a number is the biggest number that is equal to or smaller than the target.
def FloorNumber(nums, target):
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
        return end


index = FloorNumber(nums, target)
print('Floor of a number: ' + str(nums[index]))