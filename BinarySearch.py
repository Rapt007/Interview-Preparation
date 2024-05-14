
nums = [-1, 0, 3, 5, 9, 12]
target = 55

def BinarySearch(nums, target):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = start + int((end - start) / 2)
        print(mid)
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            start = mid + 1
        else:
            end = mid - 1

    else:
        return -1


index = BinarySearch(nums, target)
print('Target is at index:' + str(index))